from .Context import Context

class Script:

    def __init__(self, ctx, script=None):
        assert isinstance(ctx, Context)
        self.context = ctx
        if script:
            assert isinstance(script, function)
            self.script = script

    def loadScript(self, script):
        assert isinstance(script, function)
        self.script = script

    def runScript(self):
        raise ValueError('The script is not loaded in the class')