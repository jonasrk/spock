<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="/static/psicraft_webinterface.css">
        <script src="/static/psicraft_webinterface.js"></script>
    </head
    <body>
        
        <button onclick="send_command(&quot;http://localhost:8080/connect/x+&quot;)">x+</button>
        <button onclick="send_command(&quot;http://localhost:8080/connect/x-&quot;)">x-</button>
        <button onclick="send_command(&quot;http://localhost:8080/connect/z+&quot;)">z+</button>
        <button onclick="send_command(&quot;http://localhost:8080/connect/z-&quot;)">z-</button>
        <button onclick="send_command(&quot;http://localhost:8080/button/pxp&quot;)">peek@x+</button>
        <button onclick="send_command(&quot;http://localhost:8080/button/pxm&quot;)">peek@x-</button>
        <button onclick="query_and_draw()">draw chunk</button>
        <button onclick="redraw_vis()">draw chunk continuously</button>
        <button onclick="stop_redraw_vis()">stop drawing chunk continuously</button>
        <button onclick="more_layers()">more layers</button>
        <button onclick="fewer_layers()">fewer layers</button>
        <button onclick="send_command(&quot;http://localhost:8080/connect/x+&quot;)">connect to bot</button>
        
        <div id="layer_div">16 layers</div>
        
        <p><textarea id="log_area" cols="70"></textarea></p>
        
        <div class="wrapper">
            <canvas id="ChunkCanvas" width="1000" height="600"></canvas>
            <canvas id="BotCanvas" width="1000" height="600"></canvas>
        </div>
        
    </body>
</html>