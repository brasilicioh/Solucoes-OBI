import subprocess
import sys, os
import time

args: list[str] = sys.argv

if len(args) < 2:
    exit("Esperava arquivo para validar")
if args[1].endswith(".py"):
    extensao = "python"
elif args[1].endswith(".cpp") or args[1].endswith(".c"):
    extensao = "gcc"
else:
    exit("Esperava arquivo .py, .c ou .cpp")

def validate_answer(result, answer):
    result = result.strip().replace('\r\n', '\n')
    answer = answer.strip().replace('\r\n', '\n')
    return result == answer

def run_program(cmd, input_file):
    program = subprocess.Popen(cmd,
                stdin=input_file,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True)
    startCode = time.perf_counter()
    stdout, stderr = program.communicate()
    endCode = time.perf_counter()
    if program.returncode != 0:
        print(stderr)
    return [stdout, stderr, endCode-startCode]

base_name = os.path.splitext(os.path.basename(args[1]))[0]
program_path = os.path.join("solucoes", base_name, args[1])
folder_name = os.path.join("checks", base_name)

if extensao == "gcc":
    exe_path = os.path.join("solucoes", base_name, base_name + ".exe")
    compiler = "g++" if args[1].endswith(".cpp") else "gcc"
    compile_cmd = [compiler, "-O2", "-std=c++17"] if args[1].endswith(".cpp") else [compiler, "-O2"]
    compile_cmd += [program_path, "-o", exe_path]
    proc = subprocess.run(compile_cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        print("Erro de compilação:")
        print(proc.stderr)
        exit(1)
    run_cmd = [exe_path]
else:
    run_cmd = ["python", program_path]

tests_needed = len([name for name in os.listdir(os.path.join(os.getcwd(), folder_name))])
timesCode = []
for test in range(tests_needed):
    check_path = folder_name + "\\" + str(test+1)
    print(check_path)
    checks_needed = len([name for name in os.listdir(os.path.join(os.getcwd(), check_path))]) // 2

    print(f"Teste {test + 1}:")

    #loop through checks
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
            print(f"  Check {i} está correto - {exeCount:.6f}")
            timesCode.append(exeCount)
        else:
            print(f"  Check {i} está incorreto")
    
print(f"\nMax time: {max(timesCode):.6f}")