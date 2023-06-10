import os
import ezkl

# HERE WE SETUP THE CIRCUIT PARAMS
# WE GOT KEYS
# WE GOT CIRCUIT PARAMETERS
# EVERYTHING ANYONE HAS EVER NEEDED FOR ZK

def main():
    params_path = os.path.join('kzg.params')
    res = ezkl.gen_srs(params_path, 17)

    model_path = os.path.join('network.onnx')
    pk_path = os.path.join('test.pk')
    vk_path = os.path.join('test.vk')
    circuit_params_path = os.path.join('circuit.params')
    params_path = os.path.join('kzg.params')

    res = ezkl.setup(
            model_path,
            vk_path,
            pk_path,
            params_path,
            circuit_params_path,
        )

    assert res == True
    assert os.path.isfile(vk_path)
    assert os.path.isfile(pk_path)
    assert os.path.isfile(circuit_params_path)

if __name__ == "__main__":
    main()