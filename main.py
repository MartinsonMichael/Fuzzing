import numpy as np
import string
import os


def generate_random_string(size: int):
    """Generate random string with a given length"""
    return "".join(np.random.choice(
        list(string.ascii_letters + string.digits), size)
    )


def test_cat(test_num: int, str_size) -> float:
    """Test given system function"""
    success = 0
    for _ in range(test_num):
        current_input = generate_random_string(str_size)
        try:
            with open("temp", "w") as file:
                file.write(current_input)
            stream = os.popen(f"cat temp")
            output = stream.read()
            if output == current_input:
                success += 1
        except:
            pass
    return success / test_num


def test_echo(test_num: int, str_size) -> float:
    """Test given system function"""
    success = 0
    for _ in range(test_num):
        current_input = generate_random_string(str_size)
        try:
            stream = os.popen(f'echo -n {current_input}')
            output = stream.read()
            if output == current_input:
                success += 1
        except:
            pass
    return success / test_num


def main():
    NUM_TESTS = 1000
    STRING_SIZE = 20

    print("========== Test cat ==========")
    success_ratio = test_cat(NUM_TESTS, STRING_SIZE)
    print(f"Success ration for cat is {success_ratio}\n")

    print("========== Test echo ==========")
    success_ratio = test_echo(NUM_TESTS, STRING_SIZE)
    print(f"Success ration for echo is {success_ratio}\n")


if __name__ == "__main__":
    main()
