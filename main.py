from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Serves style.css and any images/assets you add later under /static
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"active": "home"},
    )


@app.get("/about")
def about(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="about.html",
        context={"active": "about"},
    )

# --- Your turn ---
# Add /skills, /projects, /blog, /contact, /resume the exact same way:
#   1. Copy templates/about.html -> templates/skills.html, change the content
#   2. Add a route here, same shape as about() above:
#
#      @app.get("/skills")
#      def skills(request: Request):
#          return templates.TemplateResponse(
#              "skills.html", {"request": request, "active": "skills"}
#          )
#
#   3. Run it, look at it, deploy, then repeat for the next page.
