from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from plotly import graph_objs
from plotly import offline

from line_graph.models import RateData
from line_graph.form import RateDataForm


def index(request):
    line_graph_data = RateData.objects.order_by('datetime', 'rate', 'id')

    rate_dict = {'line_graph_data': line_graph_data}
    #create_rate_line_graph(rate_dict)
    return render(request, 'line_graph/index.html', context=rate_dict)


def edit(request, id=None):
    if id:
        ratedata = get_object_or_404(RateData, pk=id)
    else:
        ratedata = RateData()

    if request.method == 'POST':

        form = RateDataForm(request.POST, instance=ratedata)
        if form.is_valid():
            ratedata = form.save(commit=False)
            ratedata.save()
            return redirect('line_graph:index')
    else:
        form = RateDataForm(instance=ratedata)

    return render(request, 'line_graph/edit.html', dict(form=form, id=id))




def delete(request):
    ratedata = get_object_or_404(RateData, pk=id)
    ratedata.delete()
    return redirect('line_graph:index')


def create_rate_line_graph(rate_lists_dic):
    """
    Create rate graph as html file

    :param rate_lists [django.db.models.query.QuerySet]: treatRateData model class's data
    """
    date = []
    rate = []

    for acc in rate_lists_dic['line_graph_data']:
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


def graph(request):
    line_graph_data = RateData.objects.order_by('datetime', 'rate')

    rate_dict = {'line_graph_data': line_graph_data}
    create_rate_line_graph(rate_dict)
    return render(request, 'line_graph/graph.html', context=rate_dict)