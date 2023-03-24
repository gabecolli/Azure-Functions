# the init is the actual function.

In `function.json` the `name` parameter must not change its value. the request fails for some reason.
for example instead of `name` use `othername` it will fail.

### on the init file

`req` is the actually request object being sent to the api.
need to declare `req.get_json()` into a variable to get the contents of the object. this is excluding any headers.
