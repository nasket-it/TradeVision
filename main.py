from dach_chart_tv import app









if __name__ == '__main__':
    port = 80
    host = '185.225.34.60'
    app.run_server(debug=False, host=host, port=port)