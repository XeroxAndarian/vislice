% import model
<!DOCTYPE html>
<html>

<head>
    <title>Vislice</title>
</head>

<body>


    <table>
        <tr>
            <td>
                {{ igra.pravilni_del_gesla()  }}
            </td>
        </tr>
        <tr>
            <td>
                Neuspeli poskusi:
            </td>
            <td>
                {{ igra.nepravilni_ugibi()  }}
            </td>
        </tr>

        % if poskus == model.ZMAGA:

        <form action="/igra/" method="POST">
        <input type="submit" value="Nova Igra">
        </form>
        
        Uspešno ste uganili vse črke :D
        
        % elif poskus == model.PORAZ:

        <form action="/igra/" method="POST">
        <input type="submit" value="Nova Igra">
        </form>

        Več sreče prihodnjič :(

        % else:
        <tr>
            <form action="/igra/{{id_igre}}/" method="POST">
                <input type="text" name="poskus">
                <input type="submit" value="Oddaj">
            </form>
        </tr>
        <tr>
                <form action="/" method="GET">
                    <input type="submit" value="Na začetno stran">
                </form>
            </tr>

        % end
    </table>
    


</body>

</html>