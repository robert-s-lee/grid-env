Grid can run any Python code with *Zero Modifications*.
This tutorial provides an overview on how *Zero Modifications* is accomplished.
To follow this tutorial, please sign up for free [Community Grid](https://www.grid.ai/). 
Optionally, join [Community Slack](http://gridai-community.slack.com/) and review [Docs](https://docs.grid.ai/).

With Grid, Python code does not require any specific library or hooks to be present.
Fundamentally, Grid automatically: 
- examines the code 
- provisions container image with all dependencies 
- caches this image for reuse
- provisions K8s pods
- mounts storage devices including training data
- runs the code
- saves all artifacts

The container image and K8s pods can be fine tuned with 
the standard Python `requirement.txt` and Grid specific `.yaml` files.
Grid can be treated as a black box.
Understanding the input, output, observing the behavior, and affecting the behavior can maximize the benefits. 

# Run any Python code

Lets look at command line arguments, storage devices, and OS.  Working directory and File Systems mounts are different as expected.

For those on OSX, Linux, Windows:

- Access to Grid
```bash
conda create -name gridai --python=3.8.5
conda activate gridai
pip install lightning-grid
grid login --username xxxx --key xxxx
```
- Obtain the sample code
```bash
git clone https://github.com/robert-s-lee/argecho
cd argecho 
```
- Run the code locally and Grid
```bash
python   argecho.py --arg1 1 --arg2 2
grid run argecho.py --arg1 1 --arg2 2
```
The output from local:
```bash
% python   argecho.py --arg1 1 --arg2 2

Arguments:
Number of arguments: 5 arguments.
Argument List: ['argecho.py', '--arg1', '1', '--arg2', '2']

Working Directory:
os.getcwd=/Users/rslee/github/argecho

File Systems Mounted:
Filesystem       Size   Used  Avail Capacity iused      ifree %iused  Mounted on
/dev/disk1s5s1   251G    23G    31G    43%  559993 2447541327    0%   /
```


The output from Grid:
```bash
Arguments:
Number of arguments: 5 arguments.
Argument List: ['argecho.py', '--arg1', '1', '--arg2', '2']

Working Directory:
os.getcwd=/gridai/project

File Systems Mounted:
Filesystem      Size  Used Avail Use% Mounted on
overlay         108G  8.4G  100G   8% /
tmpfs            68M     0   68M   0% /dev
tmpfs           2.1G     0  2.1G   0% /sys/fs/cgroup
/dev/xvda1      108G  8.4G  100G   8% /etc/hosts
tmpfs           2.1G     0  2.1G   0% /dev/shm
tmpfs           2.1G   13k  2.1G   1% /run/secrets/kubernetes.io/serviceaccount
tmpfs           2.1G     0  2.1G   0% /proc/acpi
tmpfs           2.1G     0  2.1G   0% /proc/scsi
tmpfs           2.1G     0  2.1G   0% /sys/firmware
```

# What is the OS Image

```bash
% grid run argecho.py --arg1 1 --arg2 2
WARNING Neither a CPU or GPU number was specified. 1 CPU will be used as a default. To use N GPUs pass in '--grid_gpus N' flag.

                Run submitted!
                `grid status` to list all runs
                `grid status spiffy-sunfish-821` to see all experiments for this run

                ----------------------
                Submission summary
                ----------------------
                script:                  argecho.py
                instance_type:           t2.medium
                use_spot:                False
                cloud_provider:          aws
                cloud_credentials:       cc-qdfdk
                grid_name:               spiffy-sunfish-821
                datastore_name:          None
                datastore_version:       None
                datastore_mount_dir:     None

```

```bash
% grid status
✔ Done!
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━┓
┃ Run                  ┃              Project ┃ Status ┃    Duration ┃ Experiments ┃ Running ┃ Queued ┃ Completed ┃ Failed ┃ Stopped ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━┩
│ lurking-seahorse-950 │ robert-s-lee/argecho │ queued │ 0d-00:02:12 │           1 │       0 │      1 │         0 │      0 │       0 │
└──────────────────────┴──────────────────────┴────────┴─────────────┴─────────────┴─────────┴────────┴───────────┴────────┴─────────┘

36 Run(s) are not active. Use `grid history` to view your Run history.
✔ Loading Interactive Nodes...
┏━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━┓
┃ Name       ┃ Status ┃ Instance Type ┃    Duration ┃ URL ┃
┡━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━┩
│ test       │ paused │     t2.medium │ 3d-05:52:41 │   - │
│ rsleemnist │ paused │     t2.medium │ 7d-21:19:39 │   - │
└────────────┴────────┴───────────────┴─────────────┴─────┘
```

# New Container Image the first time

```bash
% grid logs lurking-seahorse-950-expo

#1 [internal] load .dockerignore
#1 sha256:2891c97ac248f2c635407e8b3317d2eeafb9765c0e5be20faae93b057eef3e20
#1 transferring context: 1.40kB done
#1 DONE 0.0s

#2 [internal] load build definition from Dockerfile
#2 sha256:e3b8a23a1d4333ee59e25ae7eebd54ba6d4de075310e0e299c2916c12d09ff32
#2 transferring dockerfile: 919B done
#2 DONE 0.0s

#4 [auth] sharing credentials for ******
#4 sha256:ec0c71a19b372a4526a4af8fe0796bcb06f45989df362231c6426e3f13caaffa
#4 DONE 0.0s

#3 [internal] load metadata for ******/*******************/grid-images__cpu-ubuntu18.04-py3.8-torch1.7.1-pl1.2.1:manual-v11
#3 sha256:4540001f5a12c554b7786650ec54b1b8863d8fff62177230e535c46a72d24e8a
#3 DONE 0.2s

#5 [1/5] FROM ******/*******************/grid-images__cpu-ubuntu18.04-py3.8-torch1.7.1-pl1.2.1:manual-v11@sha256:181b4da827cd281228f4031893d27b848c1d3fb082de98ab3063def79397987b
#5 sha256:84322125a6416abfae49b8b9db1fb113872d038a42a582c13c0230622eac03cc
#5 DONE 0.0s

#8 [internal] load build context
#8 sha256:5289e3f8dad299c21c82d8d5931d5997e2c0de3281f1793caa7352ed54535aee
#8 transferring context: 68.97kB 0.0s done
#8 DONE 0.0s

#6 [2/5] RUN mkdir -p /gridai/project
#6 sha256:81fd188b4a24485284ab4b0b9e5fdd7224a9d3c54acc4194937d11c1253a1877
#6 CACHED

#7 [3/5] WORKDIR /gridai/project
#7 sha256:9760fc3a0d9095e7bce9c21b3e431b6ca9a5bd5f6297f141f6ecef67052ffe70
#7 CACHED

#9 [4/5] COPY / /gridai/project/
#9 sha256:faaadeb1dc106a72aca8998b072800d64cb043db5c6e526845cc8944b4df743c
#9 DONE 0.0s

#10 [5/5] RUN echo "Beginning Project Specific Installations" &&     echo "Finished Project Specific Installations"
#10 sha256:95f3bf0e474a18e4b9dd2ce94cebd70b407455325a7ffe1aba9d7fd1b96ce371
#10 0.480 Beginning Project Specific Installations
#10 0.480 Finished Project Specific Installations
#10 DONE 0.5s

#11 exporting to image
#11 sha256:e8c613e07b0b7ff33893b694f7759a10d42e180f2b4dc349fb57dc6b71dcab00
#11 exporting layers 0.1s done
#11 writing image sha256:0c5e6e970377147765ff1e76c6675da7e528dfbfa57655fdfd6b133f6ef2b8d8 done
#11 naming to ******/*******************/robert-s-lee__argecho-cpu:f2abb8dd2401638142230e57ef07612104f5784e-f6aedbcc5bbd6b76cfdd792164f4b9bf done
#11 DONE 0.1s
Experiment is pending. Logs will be available when experiment starts.
```

- when the run is complete, it will no longer show on `grid status` command.  

```bash
% grid status
✔ Done!
┏━━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━┓
┃ Run          ┃ Project ┃ Status ┃ Duration ┃ Experiments ┃ Running ┃ Queued ┃ Completed ┃ Failed ┃ Stopped ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━┩
│ None Active. │         │        │          │             │         │        │           │        │         │
└──────────────┴─────────┴────────┴──────────┴─────────────┴─────────┴────────┴───────────┴────────┴─────────┘

38 Run(s) are not active. Use `grid history` to view your Run history.
✔ Loading Interactive Nodes...
┏━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━┓
┃ Name       ┃ Status ┃ Instance Type ┃    Duration ┃ URL ┃
┡━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━┩
│ test       │ paused │     t2.medium │ 3d-05:57:38 │   - │
│ rsleemnist │ paused │     t2.medium │ 7d-21:24:37 │   - │
└────────────┴────────┴───────────────┴─────────────┴─────┘
```

- Per instruction above, use `grid history` to view Run history.  The list is sorted by the `Created At` date.

```bash
 % grid history
✔ Done!
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━┳━━━━━━━━━━━┓
┃ Run                       ┃               Created At ┃ Experiments ┃ Failed ┃ Stopped ┃ Completed ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━╇━━━━━━━━━━━┩
│ spiffy-sunfish-821        │ 2021-06-12 17:13:54+0000 │           1 │      0 │       0 │         1 │
│ lurking-seahorse-950      │ 2021-06-12 17:09:56+0000 │           1 │      0 │       0 │         1 │
│ winged-puma-326           │ 2021-06-11 17:02:31+0000 │           1 │      0 │       0 │         1 │
│ uptight-starling-342      │ 2021-06-11 16:43:54+0000 │           1 │      0 │       0 │         1 │
│ functional-bandicoot-549  │ 2021-06-11 16:28:34+0000 │           1 │      1 │       0 │         0 │
│ nifty-cuttlefish-238      │ 2021-06-11 16:17:06+0000 │           1 │      1 │       0 │         0 │
│ manipulative-newt-557     │ 2021-06-11 15:59:18+0000 │           1 │      1 │       0 │         0 │
```

# Reuse Cached Container Image the sunsequent time


```bash
 % grid logs crystal-ermine-224-exp0
[stdout] [2021-06-12T17:24:11.162831+00:00] Arguments:
[stdout] [2021-06-12T17:24:11.162879+00:00] Number of arguments: 2 arguments.
[stdout] [2021-06-12T17:24:11.162884+00:00] Argument List: ['argecho.py', '--test']
[stdout] [2021-06-12T17:24:11.162888+00:00]
[stdout] [2021-06-12T17:24:11.162892+00:00] Working Directory:
[stdout] [2021-06-12T17:24:11.162896+00:00] os.getcwd=/gridai/project
[stdout] [2021-06-12T17:24:11.162899+00:00]
[stdout] [2021-06-12T17:24:11.162903+00:00] File Systems Mounted:
[stdout] [2021-06-12T17:24:11.162907+00:00] Filesystem      Size  Used Avail Use% Mounted on
[stdout] [2021-06-12T17:24:11.162910+00:00]
[stdout] [2021-06-12T17:24:11.162914+00:00] Python Version:
[stdout] [2021-06-12T17:24:11.162918+00:00] 3.8.5 (default, Sep  4 2020, 07:30:14)
[stdout] [2021-06-12T17:24:11.162921+00:00] [GCC 7.3.0]
[stdout] [2021-06-12T17:24:11.162925+00:00]
[stdout] [2021-06-12T17:24:11.162928+00:00] Python Packages:
[stdout] [2021-06-12T17:24:11.162935+00:00] ['absl-py==0.12.0', 'aiohttp==3.7.4.post0', 'alembic==1.4.1', 'async-timeout==3.0.1', 'attrs==21.2.0', 'bravado-core==5.17.0', 'bravado==11.0.3', 'brotlipy==0.7.0', 'cachetools==4.2.2', 'certifi==2020.12.5', 'cffi==1.14.3', 'chardet==3.0.4', 'click==8.0.1', 'cloudpickle==1.6.0', 'comet-ml==3.10.0', 'conda-package-handling==1.7.2', 'conda==4.10.1', 'configobj==5.0.6', 'configparser==5.0.2', 'cryptography==3.2.1', 'databricks-cli==0.14.3', 'docker-pycreds==0.4.0', 'docker==5.0.0', 'dulwich==0.20.23', 'entrypoints==0.3', 'everett==1.0.3', 'flask==2.0.1', 'fsspec==2021.5.0', 'future==0.18.2', 'gitdb==4.0.7', 'gitpython==3.1.17', 'google-auth-oauthlib==0.4.4', 'google-auth==1.30.1', 'greenlet==1.1.0', 'grpcio==1.38.0', 'gunicorn==20.1.0', 'idna==2.10', 'imageio==2.9.0', 'itsdangerous==2.0.1', 'jinja2==3.0.1', 'jsonref==0.2', 'jsonschema==3.2.0', 'mako==1.1.4', 'markdown==3.3.4', 'markupsafe==2.0.1', 'mkl-fft==1.3.0', 'mkl-random==1.2.1', 'mkl-service==2.3.0', 'mlflow==1.17.0', 'monotonic==1.6', 'msgpack==1.0.2', 'multidict==5.1.0', 'neptune-client==0.9.15', 'numpy==1.20.2', 'nvidia-ml-py3==7.352.0', 'oauthlib==3.1.0', 'olefile==0.46', 'packaging==20.9', 'pandas==1.2.4', 'pathtools==0.1.2', 'pillow==8.2.0', 'pip==20.2.4', 'prometheus-client==0.10.1', 'prometheus-flask-exporter==0.18.2', 'promise==2.3', 'protobuf==3.17.1', 'psutil==5.8.0', 'pyasn1-modules==0.2.8', 'pyasn1==0.4.8', 'pycosat==0.6.3', 'pycparser==2.20', 'pyjwt==2.1.0', 'pyopenssl==19.1.0', 'pyparsing==2.4.7', 'pyrsistent==0.17.3', 'pysocks==1.7.1', 'python-dateutil==2.8.1', 'python-editor==1.0.4', 'pytorch-lightning==1.2.1', 'pytz==2021.1', 'pyyaml==5.3.1', 'querystring-parser==1.2.4', 'requests-oauthlib==1.3.0', 'requests-toolbelt==0.9.1', 'requests==2.24.0', 'rsa==4.7.2', 'ruamel-yaml==0.15.87', 'sentry-sdk==1.1.0', 'setuptools==50.3.1.post20201107', 'shortuuid==1.0.1', 'simplejson==3.17.2', 'six==1.15.0', 'smmap==4.0.0', 'sqlalchemy==1.4.15', 'sqlparse==0.4.1', 'subprocess32==3.5.4', 'swagger-spec-validator==2.7.3', 'tabulate==0.8.9', 'tensorboard-data-server==0.6.1', 'tensorboard-plugin-wit==1.8.0', 'tensorboard==2.5.0', 'test-tube==0.7.5', 'torch==1.7.1', 'torchaudio==0.7.0a0+a853dff', 'torchvision==0.8.2', 'tqdm==4.51.0', 'typing-extensions==3.7.4.3', 'urllib3==1.25.11', 'wandb==0.10.30', 'websocket-client==1.0.1', 'werkzeug==2.0.1', 'wheel==0.35.1', 'wrapt==1.12.1', 'wurlitzer==2.1.0', 'yarl==1.6.3']
```