katex_template = """
<!DOCTYPE html>
<div id="printButton">
    <style>
        svg {{
            position: fixed;
            right: 20px;
            padding: 10px;
            transition: fill 0.3s ease;
        }}

        svg:hover {{
            fill: #f9423a;
        }}
    </style>

    <script>
        function openPrintPopup() {{
            const contentToPrint = document.getElementById('printSection').innerHTML;

            const printWindow = window.open('', '_blank', 'width=800,height=600');

            printWindow.document.open();
            printWindow.document.write(contentToPrint);
            printWindow.document.close();

            printWindow.focus();
            printWindow.print();
        }}
    </script>

    <svg onclick="openPrintPopup()" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" role="button">
        <title>Print</title>
        <path d="M18 3H6v4h12m1 5a1 1 0 0 1-1-1 1 1 0 0 1 1-1 1 1 0 0 1 1 1 1 1 0 0 1-1 1m-3 7H8v-5h8m3-6H5a3 3 0 0 0-3 3v6h4v4h12v-4h4v-6a3 3 0 0 0-3-3Z"></path>
    </svg>
</div>
<div id="printSection">
<head>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.19/dist/katex.min.css" integrity="sha384-7lU0muIg/i1plk7MgygDUp3/bNRA65orrBub4/OSWHECgwEsY83HaS1x3bljA/XV" crossorigin="anonymous">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.19/dist/katex.min.js" integrity="sha384-RdymN7NRJ+XoyeRY4185zXaxq9QWOOx3O7beyyrRK4KQZrPlCDQQpCu95FoCGPAE" crossorigin="anonymous"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.19/dist/contrib/auto-render.min.js" integrity="sha384-hCXGrW6PitJEwbkoStFjeJxv+fSOOQKOPbJxSfM6G5sWZjAyWhXiTIIAmQqnlLlh" crossorigin="anonymous"></script>
<script>
    document.addEventListener("DOMContentLoaded", function() {{
        renderMathInElement(document.body, {{
          // • rendering keys, e.g.:
          throwOnError : false
        }});
    }});
</script>
<style>
    @font-face {{
        font-family: KaTeX_Math;
        font-style: normal;
        font-weight: 400;
        src: url(fonts/KaTeX_Math-Regular.woff2) format("woff2"),url(fonts/KaTeX_Math-Regular.woff) format("woff"),url(fonts/KaTeX_Math-Regular.ttf) format("truetype")
    }}

    .katex {{
        line-height: 1.6;
    }}

    .katex .mathnormal {{
        font-family: KaTeX_Math;
        font-style: normal;
    }}

    .katex-display>.katex {{
        text-align: left;
    }}

    .structural-class {{
        display: block;
        padding: 5px;
        font-size: 1.2em;
    }}

    .blueprints {{
        position: fixed;
        right: 20px;
        bottom: 20px;
        padding: 10px;
        background-color: rgba(255, 255, 255, 0.5);
    }}

    #myFormula .katex .base,
    #myFormula .katex .base span,
    #myFormula .katex .strut {{
        white-space: normal !important;
        width: auto !important;
        max-width: 100% !important;
    }}


</style>


</head>
<body>
    <h2>Calculation of the nominal concrete cover according to <br>
    Eurocode 1992-1-1:2005+A1:2015+NB:2016+A1:2020</h2>
    <div id="myFormula">
        $$
        {nominal_cover_calculation}
        $$
    </div>

    <div class="structural-class">
        Structural class is determined according to table 4.3: {structural_class}
    </div>

    <div class="blueprints">
        <p>Powered by
            <a href="https://blueprints.readthedocs.io" target="_blank">Blueprints</a>
        <br>The open-source Python package for civil engineering.
        </p>
    </div>

</body>
</div>
</html>
"""
