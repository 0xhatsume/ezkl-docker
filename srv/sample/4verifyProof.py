import ezkl
import os

def main():
    # from previous params
    proof_path = os.path.join('test.pf')
    circuit_params_path = os.path.join('circuit.params')
    vk_path = os.path.join('test.vk')
    params_path = os.path.join('kzg.params')

    res = ezkl.verify(
            proof_path,
            circuit_params_path,
            vk_path,
            params_path,
        )

    assert res == True
    print(f"verified: {res}")


if __name__ == "__main__":
    main()