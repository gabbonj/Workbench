
class Script:

    def __init__(self, ctx, obj=None,  start_script=None, update_script=None):
        self.context = ctx
        if obj:
            self.object = obj

        if start_script:
            self.startScript = lambda : start_script(self)
        else:
            self.startScript = None

        if update_script:
            self.updateScript = lambda : update_script(self)
        else:
            self.updateScript = None


    def loadScripts(self, start_script, update_script):
        self.startScript = lambda : start_script(self)
        self.updateScript = lambda : update_script(self)
