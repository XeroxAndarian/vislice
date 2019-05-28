% rebase('base.tpl')


<table>
    <tr>
        <td>
           Za pričetek pritisnite gumb
        </td>
    </tr>
    <tr>
        <form action="/nova_igra/" method="POST">
        
            <input type="submit" value="Nova Igra">
           
        </form>

        <form action="/odpri_igra/" method="POST">
            <input type="text" name="id_igre">
            <input type="submit" value="Odpri">
           
        </form>
        
    </tr>
</table>
    

