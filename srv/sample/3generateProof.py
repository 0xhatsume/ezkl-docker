import os
import ezkl

def main():
    # from previous setp
    model_path = os.path.join('network.onnx')
    pk_path = os.path.join('test.pk')
    circuit_params_path = os.path.join('circuit.params')
    params_path = os.path.join('kzg.params')

    # new paths
    proof_path = os.path.join('test.pf')
    data_path = os.path.join('input.json')

    res = ezkl.prove(
            data_path,
            model_path,
            pk_path,
            proof_path,
            params_path,
            "poseidon",
            "single",
            circuit_params_path
        )

    assert res == True
    assert os.path.isfile(proof_path)

if __name__ == "__main__":
    main()