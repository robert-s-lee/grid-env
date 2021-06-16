
```bash
# make location of training data command line argument 
curl -O https://raw.githubusercontent.com/optuna/optuna-examples/main/pytorch/pytorch_lightning_simple.py

diff pytorch_lightning_simple.py ~/github/optuna-examples/pytorch/pytorch_lightning_simple.py
129c129
<     datamodule = FashionMNISTDataModule(data_dir=args.datadir, batch_size=BATCHSIZE)
---
>     datamodule = FashionMNISTDataModule(data_dir=DIR, batch_size=BATCHSIZE)
155d154
<     parser.add_argument('--datadir', default=f'{os.getcwd()}', type=str)
```

```bash
# run on local  
mkdir data
pip install optuna
pip install pytorch_lightning
pip install torchvision
python pytorch_lightning_simple.py --datadir ./data
python pytorch_lightning_simple.py --datadir ./data --pruning
```

```bash
# setup datastore for repeat run on VMs  
grid datastore create --source data --name fashionmnist 

# setup datastore for repeat run on VMs  

% grid datastore list
┏━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ Credential Id ┃              Name ┃ Version ┃     Size ┃          Created ┃    Status ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━┩
│ cc-qdfdk      │      fashionmnist │       7 │ 141.6 MB │ 2021-06-16 15:13 │ Succeeded │

```

Interesting things to note:
- checks for uncommiteed files (which we can safely README.md)
- scanned code and automagically will setup the environment with `torchvision`, `packaging`, `torch` and `pytorch_lightning` which had to be done manually on laptop
- `grid:fashionmnist:7` is a short hand for fashionmnist datastore version 7

```bash
grid run pytorch_lightning_simple.py --datadir grid:fashionmnist:7

WARNING Neither a CPU or GPU number was specified. 1 CPU will be used as a default. To use N GPUs pass in '--grid_gpus N' flag.


    WARNING

    The following files are uncommited. Changes made to these
    files will not be avalable to Grid when running an Experiment.

      optuna/README.md

    Would you like to continue?

    You can use the flag --ignore_warnings to skip this warning.
    See details at: https://docs.grid.ai

    [y/N]: y


        WARNING
        No requirements.txt or environment.yml found but we identified below
        dependencies from your source. Your build could crash or not
        start.

        torchvision
        packaging
        torch
        pytorch_lightning


                Run submitted!
                `grid status` to list all runs
                `grid status micro-rhino-434` to see all experiments for this run

                ----------------------
                Submission summary
                ----------------------
                script:                  pytorch_lightning_simple.py
                instance_type:           t2.medium
                use_spot:                False
                cloud_provider:          aws
                cloud_credentials:       cc-qdfdk
                grid_name:               micro-rhino-434
                datastore_name:          None
                datastore_version:       None
                datastore_mount_dir:     None
```