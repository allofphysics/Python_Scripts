import pandas as pd


def html_gen(csv_file, html_file):
    tf = pd.read_csv(csv_file, names=range(3))  # may need to add names for columns
    f = open(html_file, "w")
    f.write(
        '<link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/v/dt/jq-2.2.4/dt-1.10.13/r-2.1.0/datatables.min.css"/>'
    )
    f.write("\n")
    f.write(
        '<script type="text/javascript" src="https://cdn.datatables.net/v/dt/jq-2.2.4/dt-1.10.13/r-2.1.0/datatables.min.js"></script>'
    )
    f.write("\n")
    strng = '<table id="example" class="display nowrap dataTable dtr-inline" role="grid" aria-describedby="example_info" style="width: 100%;" width="100%" cellspacing="0">'
    tf = tf.fillna("")
    f.write(
        tf.to_html(escape=False)
        .encode("utf-8")
        .replace('<table border="1" class="dataframe">', strng)
    )
    f.write("\n")
    func = """$(document).ready(function(){
        $('#example').DataTable();
    });"""
    f.write("\n")
    f.write('<script type="text/javascript">')
    f.write("\n")
    f.write(func)
    f.write("\n")
    f.write("</script>")
    f.close()


url = "https://raw.githubusercontent.com/dhawaljoh/kaggle--data-science-london/master/test.csv"
f = open("train.csv", "w")
f.write(requests.get(url).content)
f.close()
html_gen("train.csv", "test.html")
