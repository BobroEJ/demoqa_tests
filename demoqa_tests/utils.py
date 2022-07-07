from pathlib import Path

import demoqa_tests


def resource(path):
    return str(Path(demoqa_tests.__file__).parent.parent.joinpath(f'resources/{path}'))
