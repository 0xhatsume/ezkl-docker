import os
import ezkl


def main():
    # from previous examples
    vk_path = os.path.join('test.vk')
    params_path = os.path.join('kzg.params')
    circuit_params_path = os.path.join('circuit.params')
    deployment_code_path = os.path.join('test.code')
    sol_code_path=os.path.join('test.sol')

    res = ezkl.create_evm_verifier(
        vk_path,
        params_path,
        circuit_params_path,
        deployment_code_path,
        sol_code_path
    )
    print(f"solc verifier created: {res}")


if __name__ == "__main__":
    main()