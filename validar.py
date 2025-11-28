import subprocess
import tempfile
import sys
import os
import time

def validate_answer(result: str, answer: str) -> bool:
    result = result.strip().replace('\r\n', '\n')
    answer = answer.strip().replace('\r\n', '\n')
    return result == answer

def run_program(cmd, input_file) -> list:
    program = subprocess.Popen(cmd,
                stdin=input_file,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True)
    startCode = time.perf_counter()
    stdout, stderr = program.communicate()
    endCode = time.perf_counter()
    return [stdout, stderr, endCode-startCode]

args: list[str] = sys.argv

if len(args) < 2:
    exit("Esperava arquivo para validar")
if args[1].endswith(".py"):
    extensao = "python"
elif args[1].endswith(".cpp") or args[1].endswith(".c"):
    extensao = "gcc"
elif args[1].endswith(".js"):
    extensao = "javascript"
elif args[1].endswith(".rs"):
    extensao = "rust"
else:
    exit("Esperava arquivo .py, .c, .cpp, .js ou .rs")

base_name = os.path.splitext(os.path.basename(args[1]))[0]
program_path = os.path.join("solucoes", base_name, args[1])
folder_name = os.path.join("checks", base_name)

if extensao == "gcc":
    exe_path = os.path.join("solucoes", base_name, base_name + ".exe")
    compiler = "g++" if args[1].endswith(".cpp") else "gcc"
    compile_cmd = [compiler, "-O2", "-std=c++17"] if args[1].endswith(".cpp") else [compiler, "-O2"]
    compile_cmd += [program_path, "-o", exe_path]
    proc = subprocess.run(compile_cmd, capture_output=True, text=True)
    run_cmd = [exe_path]
elif extensao == "rust":
    exe_path = os.path.join("solucoes", base_name, base_name + ".exe")
    compile_cmd = ["rustc", "-O", program_path, "-o", exe_path]
    proc = subprocess.run(compile_cmd, capture_output=True, text=True)
    run_cmd = [exe_path]
elif extensao == "javascript":
    wrapper_code = r'''
const fs = require('fs'), input = fs.readFileSync(0, 'utf-8').split(/\s+/);
let inputIndex = 0;
function scanf(fmt, varName) {
    var value = parseInt(input[inputIndex++]);
    eval(varName + " = value");
}
function printf(fmt, value) {
    process.stdout.write(fmt.replace('%d', value));
}
'''
    with open(program_path, 'r', encoding='utf-8') as file:
        user_code = file.read()
    temp_js = tempfile.NamedTemporaryFile('w', delete=False, suffix='.js')
    temp_js.write(wrapper_code + '\n' + user_code)
    temp_js.close()
    run_cmd = ["node", temp_js.name]
else:
    run_cmd = ["python", program_path]

tests_needed = len([name for name in os.listdir(os.path.join(os.getcwd(), folder_name))])
timesCode = [0]
for test in range(tests_needed):
    check_path = folder_name + "\\" + str(test+1)
    checks_needed = len([name for name in os.listdir(os.path.join(os.getcwd(), check_path))]) // 2

    print(f"\n\033[1mTeste {test + 1}:\033[m")

    for i in range(1, checks_needed + 1):
        try:
            input_file = open(f"{check_path}\\{i}.in", "r", encoding="utf-8")
            answer_file = open(f"{check_path}\\{i}.sol", "r", encoding="utf-8")
        except:
            input_file = open(f"{check_path}\\in{i}", "r", encoding="utf-8")
            answer_file = open(f"{check_path}\\out{i}", "r", encoding="utf-8")
        answer_content = answer_file.read()
        stdout, stderr, exeCount = run_program(run_cmd, input_file)
        input_file.close()
        answer_file.close()
        if validate_answer(stdout, answer_content):
            print(f"\033[0;32m    Check {i} está correto - {exeCount:.6f}\033[m")
            timesCode.append(exeCount)
        else:
            print(f"\033[0;31m    Check {i} está incorreto\033[m")
    
print(f"\nMax time: {max(timesCode):.6f}\n" if len(timesCode) > 1 else "\n")

if extensao in ["gcc", "rust"]:
    try:
        os.unlink(exe_path)
        pdb_path = os.path.splitext(exe_path)[0] + ".pdb"
        if os.path.exists(pdb_path):
            os.unlink(pdb_path)
    except:
        pass