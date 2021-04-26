from sanic import Sanic
from sanic.response import json

app = Sanic()

@app.route('/')
async def test(request):
    return json({'Hello':'World'}) 


if __name__ == '__main__':
    app.run()
