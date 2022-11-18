'''
How to Render and Return Plot to View in Flask
'''

## Importing required functions --------------------------------
from flask import Flask, render_template
from bokeh.embed import components
from bokeh.plotting import figure

## Flask constructor -------------------------------------------
app = Flask(__name__)

## Root endpoint -----------------------------------------------
@app.route('/')
def homepage():

    ### Defining Chart Data ###
    language   = [
        'Python', 'Java', 'JavaScript', 'C#', 'PHP', 'C/C++', 
        'R', 'Objective-C', 'Swift', 'TypeScript', 'Matlab', 
        'Kotlin', 'Go', 'Ruby', 'VBA'
    ]
    popularity = [
        31.56, 16.4, 8.38, 6.5, 5.85, 5.8, 4.08, 2.79, 2.35, 
        1.92, 1.65, 1.61, 1.44, 1.22, 1.16
    ]

    ### Creating Plot Figure ###
    p = figure(
        x_range     = language,
        height      = 400,
        title       = "Popularity of Programming Languages",
        sizing_mode = "stretch_width"
    )

    ### Defining Plot to be a Vertical Bar Plot ###
    p.vbar(x = language, top = popularity, width = 0.5)
    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    ### Get Chart Components ###
    script, div = components(p)

    ### Return the components to the HTML template ###
    return render_template(
        template_name_or_list = 'charts.html',
        script  = script,
        div     = div,
    )

## Main Driver Function ----------------------------------------
if __name__ == '__main__':
    ## Run the application on the local development server ##
    app.run(debug=True)