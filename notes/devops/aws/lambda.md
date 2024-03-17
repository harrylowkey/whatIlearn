# Test lambda function

## Use the SAM CLI to build and test locally

Build your application with the `sam build --use-container` command.

```bash
rynoo-s3-test$ sam build --use-container
```

Run functions locally and invoke them with the `sam local invoke` command.

```bash
rynoo-s3-test$ sam local invoke MediaHandler --event events/event.json
```

### Notes

We need to re-build everytime we change code.
If we want to test another file, edit the key which is the file path located at s3 in events/<image/video>.json
