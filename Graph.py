from lib_repair.pyqtgraph import PlotWidget, np, mkPen

from Instances import var
from Interfaces import DataInterface
from Sections import Section


class SectionGraph(Section):
    def add_section(self):
        GraphOfCountries(self._x, self._y, self._x_span, self._y_span).add_graph()


class Graph(SectionGraph):
    def add_graph(self):
        graph_widget = PlotWidget()
        if var.get_valid():
            self.graph_display_settings(graph_widget)
        var.get_layout().addWidget(graph_widget, self._x, self._y, self._x_span, self._y_span)

    def graph_display_settings(self, graph_widget):
        pass


class GraphOfCountries(Graph):
    def add_graph(self):
        graph_widget = PlotWidget()
        graph_widget.setBackground('w')
        style = {'color': 'b', 'font-size': '18px'}
        graph_widget.setLabel('left', 'Liczba potwierdzonych przypadków', **style)
        graph_widget.setLabel('bottom', 'Kolejne dni od 22. stycznia 2020 r.', **style)
        if var.get_is_legend():
            graph_widget.addLegend()
        if var.get_valid():
            self.graph_display_settings(graph_widget)
        var.get_layout().addWidget(graph_widget, self._x, self._y, self._x_span, self._y_span)

    def graph_display_settings(self, graph_widget):
        colors = ['#0800FF', '#75FF00', '#FF0000', '#00EEFF', '#F500FF', '#FFF200', '#000000', '#FF8000', '#FF0080',
                  '#9B00FF', '#3E9400']
        color = 0
        for country in var.get_list_of_countries_to_show_on_plot():
            y = DataInterface().list_of_cases_in_country(country, var.get_data_path())
            if var.get_diff():
                y = np.diff(
                    np.array(DataInterface().list_of_cases_in_country(country, var.get_data_path()))).tolist()
            x = [j for j in range(len(y))]
            graph_widget.plot(x, y, pen=mkPen(colors[color % len(colors)], width=2), name=country)
            graph_widget.setLogMode(var.get_x_logarithmic(), var.get_y_logarithmic())
            color = color + 1
