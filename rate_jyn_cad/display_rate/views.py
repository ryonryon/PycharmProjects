from django.shortcuts import render
from django.http import HttpResponse
from display_rate.models import rateData


from plotly import graph_objs
from plotly import offline


def index(request):
    ratelists = rateData.objects.order_by('datetime', 'rate')

    rate_dict = {'rate_lists': ratelists}
    create_rate_line_graph(rate_dict)
    return render(request, 'display_rate/index.html', context=rate_dict)


def edit(request, id=None):
    return HttpResponse('Edit')


def delete(request, id=None):
    return HttpResponse('Delete')


def get_rate(request):
    return HttpResponse("Get_Today's_Rate")


def create_rate_line_graph(rate_lists_dic):
    """
    Create rate graph as html file

    :param rate_lists [django.db.models.query.QuerySet]: treatRateData model class's data
    """
    date = []
    rate = []

    for acc in rate_lists_dic['rate_lists']:
        date.append(acc.datetime)
        rate.append(acc.rate)

    line_data = graph_objs.Scatter(
        x=date,
        y=rate
    )
    data = [line_data]

    layout = graph_objs.Layout(
        title="Daily Rate JPY to CAD",
        xaxis={"title": "Datetime"},
        yaxis={"title": "Rate"},
        width=590,
        height=395,
    )

    fig = graph_objs.Figure(data=data, layout=layout)
    offline.plot(fig, filename='rate_line_graph', auto_open=False, show_link=False)