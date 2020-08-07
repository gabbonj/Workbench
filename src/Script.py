from .Context import Context

class Script:

    def __init__(self, ctx, obj=None,  script=None):
        assert isinstance(ctx, Context)
        self.context = ctx
        if obj:
            self.object = obj
        if script:
            assert isinstance(script, function)
            self.runScript = script

    def loadScript(self, script):
        self.runScript = script

    def runScript(self):
        raise ValueError('The script is not loaded in the class')