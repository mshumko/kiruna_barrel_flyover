import sys
import pathlib

# Run the configuration script when the user runs 
# python3 -m kiruna_barrel_flyover [init, initialize, config, or configure]

here = pathlib.Path(__file__).parent.resolve()


if (len(sys.argv) > 1) and (sys.argv[1] in ['init', 'initialize', 'config', 'configure']):
    print('Running the configuration script.')
    # BARREL Data dir
    s = (f'What is the BARREL data directory?')
    BARREL_DIR = input(s)
    
    # Check that the BARREL directory exists
    if not pathlib.Path(BARREL_DIR).exists():
        raise OSError(f'The BARREL diretory "{BARREL_DIR}" does not exist. Exiting.')
    
    with open(pathlib.Path(here, 'config.py'), 'w') as f:
        f.write('import pathlib\n\n')
        f.write(f'BARREL_DIR = pathlib.Path("{BARREL_DIR}")\n')
        f.write(f'PROJECT_DIR = pathlib.Path("{here}")')

else:
    print('This is a configuration script to set up config.py file. The config '
        'file will contain the BARREL data directory, and the base project '
        'directory (here). To get the prompt after this package is installed, run '
        'python3 -m kiruna_barrel_flyover init')
