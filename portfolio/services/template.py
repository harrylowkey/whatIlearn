from fastapi.templating import Jinja2Templates


class TemplateBase:
  def __init__(self):
    self.templates = Jinja2Templates(directory='portfolio/src/templates')

  def render(self, template_file, context):
    return self.templates.TemplateResponse(template_file, context)


TemplateService = TemplateBase()
