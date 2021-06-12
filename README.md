Grid reduces boilerplate codes required to run experiments. 

# What Happens on Submit

A simplest way to run a script is to issue: 
```bash
% grid run argecho.py --arg1 1 --arg2 2
``` 

This has no Grid command line argument, no Grid `.yaml`, no requirements.txt.  A script with all defaults will show a scary message `WARNING No requirements.txt or environment.yml found but we identified below dependencies from your source.Your build could crash or not start.`  Lets take step by step to see what this means.

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

```
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

# Automatic Docker Image for each Code

```
% grid logs lurking-seahorse-950-expo
[build] [2021-06-12T17:10:32.936442+00:00] #2 [internal] load .dockerignore
[build] [2021-06-12T17:10:32.938459+00:00] #2 sha256:f24086de70a1def617720b869e6f64a715032d9e95119ea19a9ea6cbafbd416f
[build] [2021-06-12T17:10:32.940141+00:00] #2 transferring context: 1.40kB done
[build] [2021-06-12T17:10:32.941547+00:00] #2 DONE 0.0s
[build] [2021-06-12T17:10:32.944168+00:00]
[build] [2021-06-12T17:10:32.946329+00:00] #1 [internal] load build definition from Dockerfile
[build] [2021-06-12T17:10:32.948228+00:00] #1 sha256:8b3217d9ee3778accf3c1a371c1fc3568587834fe34244409e5ea0008f0194f9
[build] [2021-06-12T17:10:32.950302+00:00] #1 transferring dockerfile: 919B done
[build] [2021-06-12T17:10:32.951945+00:00] #1 DONE 0.0s
[build] [2021-06-12T17:10:32.953650+00:00]
[build] [2021-06-12T17:10:32.955074+00:00] #4 [auth] sharing credentials for ******
[build] [2021-06-12T17:10:32.956382+00:00] #4 sha256:b37dee98fa18b7f3b19d84b4767874b50aacc98087533b0642816f985594e364
[build] [2021-06-12T17:10:33.037986+00:00] #4 DONE 0.0s
[build] [2021-06-12T17:10:33.039408+00:00]
[build] [2021-06-12T17:10:33.040804+00:00] #3 [internal] load metadata for ******/*******************/grid-images__cpu-ubuntu18.04-py3.8-torch1.7.1-pl1.2.1:manual-v11
[build] [2021-06-12T17:10:33.042730+00:00] #3 sha256:4540001f5a12c554b7786650ec54b1b8863d8fff62177230e535c46a72d24e8a
[build] [2021-06-12T17:10:33.044771+00:00] #3 DONE 0.2s
[build] [2021-06-12T17:10:33.046124+00:00]
[build] [2021-06-12T17:10:33.047565+00:00] #5 [1/5] FROM ******/*******************/grid-images__cpu-ubuntu18.04-py3.8-torch1.7.1-pl1.2.1:manual-v11@sha256:181b4da827cd281228f4031893d27b848c1d3fb082de98ab3063def79397987b
[build] [2021-06-12T17:10:33.049552+00:00] #5 sha256:84322125a6416abfae49b8b9db1fb113872d038a42a582c13c0230622eac03cc
[build] [2021-06-12T17:10:33.051652+00:00] #5 DONE 0.0s
[build] [2021-06-12T17:10:33.053334+00:00]
[build] [2021-06-12T17:10:33.055196+00:00] #8 [internal] load build context
[build] [2021-06-12T17:10:33.056896+00:00] #8 sha256:60ff35ccf667497c6aba05acb6020f1d7c33826055ab1f66138e5fe6b81d1d08
[build] [2021-06-12T17:10:33.187845+00:00] #8 transferring context: 35.62kB 0.0s done
[build] [2021-06-12T17:10:33.189646+00:00] #8 DONE 0.0s
[build] [2021-06-12T17:10:33.191211+00:00]
[build] [2021-06-12T17:10:33.192822+00:00] #6 [2/5] RUN mkdir -p /gridai/project
[build] [2021-06-12T17:10:33.194491+00:00] #6 sha256:81fd188b4a24485284ab4b0b9e5fdd7224a9d3c54acc4194937d11c1253a1877
[build] [2021-06-12T17:10:33.196076+00:00] #6 CACHED
[build] [2021-06-12T17:10:33.197517+00:00]
[build] [2021-06-12T17:10:33.198806+00:00] #7 [3/5] WORKDIR /gridai/project
[build] [2021-06-12T17:10:33.200079+00:00] #7 sha256:9760fc3a0d9095e7bce9c21b3e431b6ca9a5bd5f6297f141f6ecef67052ffe70
[build] [2021-06-12T17:10:33.201300+00:00] #7 CACHED
[build] [2021-06-12T17:10:33.202666+00:00]
[build] [2021-06-12T17:10:33.204075+00:00] #9 [4/5] COPY / /gridai/project/
[build] [2021-06-12T17:10:33.205453+00:00] #9 sha256:a9d816a707fc7ad2b8310777c3058fc94dd428555e80e541322e63023763c9fe
[build] [2021-06-12T17:10:33.334630+00:00] #9 DONE 0.3s
[build] [2021-06-12T17:10:33.484782+00:00]
[build] [2021-06-12T17:10:33.486307+00:00] #10 [5/5] RUN echo "Beginning Project Specific Installations" &&     echo "Finished Project Specific Installations"
[build] [2021-06-12T17:10:33.487523+00:00] #10 sha256:48c57affd992bd20c891e36532e9ef333d8da4378a0cd9b79ef0b2a95c1736d2
[build] [2021-06-12T17:10:34.045354+00:00] #10 0.606 Beginning Project Specific Installations
[build] [2021-06-12T17:10:34.046641+00:00] #10 0.606 Finished Project Specific Installations
[build] [2021-06-12T17:10:34.047828+00:00] #10 DONE 0.6s
[build] [2021-06-12T17:10:34.048907+00:00]
[build] [2021-06-12T17:10:34.049976+00:00] #11 exporting to image
[build] [2021-06-12T17:10:34.051006+00:00] #11 sha256:e8c613e07b0b7ff33893b694f7759a10d42e180f2b4dc349fb57dc6b71dcab00
[build] [2021-06-12T17:10:34.052169+00:00] #11 exporting layers 0.1s done
[build] [2021-06-12T17:10:34.084830+00:00] #11 writing image sha256:ef2ca278f3728374871c70888987b3ba1cbe731a16810cdaeae3108117fe52d1 done
[build] [2021-06-12T17:10:34.086090+00:00] #11 naming to ******/*******************/robert-s-lee__argecho-cpu:1019d109-f6aedbcc5bbd6b76cfdd792164f4b9bf done
[build] [2021-06-12T17:10:34.087231+00:00] #11 DONE 0.1s
Experiment is pending. Logs will be available when experiment starts.
```

- when the run is complete, it will no longer show on `grid status` command.  

```
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

```
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


```
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