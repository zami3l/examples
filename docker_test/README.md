Testing environments
===

Build
---
```dockerfile
$ docker build --rm -f "[PATH/dockerfile]" -t testing-env:latest "testing-env"
```

Run
---
```bash
$ docker run -ti --rm -v [MOUNT_FOLDER]:/mnt testing-env /bin/bash
```