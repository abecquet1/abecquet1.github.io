$(document).ready(function () {

    // chargement de l'affichage par défaut
    $("#programming").load("prefabs/TNSI/P_tgnsi_big.html");
    $("#algorithms").load("prefabs/TNSI/A_tgnsi_big.html");
    $("#database").load("prefabs/TNSI/BD_tgnsi_big.html");
    $("#hardware_archi").load("prefabs/TNSI/ARD_tgnsi_big.html");


    // changement du lien de l'image, indépendament du lien de la page (éviter de mettre red dans le nom de l'image)
    $(".mod_button .mod_image").hover(function () {
        var str = $(this).attr("src");

        if (str.indexOf("red") !== -1) {
            // blabla_red.png -> blabla.png
            str = str.slice(0, -8);
            str = str + ".png";
        }

        $(this).attr("src", str);
    });
    $(".mod_button .mod_image").mouseleave(function () {
        var str = $(this).attr("src");

        if (str.indexOf("red") == -1) {
            // blabla.png -> blabla_red.png
            str = str.slice(0, -4);
            str = str + "_red.png";
        }

        $(this).attr("src", str);
    });

    // gestion des clics
    // on repère le type de la liste
    // on modifie le code de la liste
    // on change le style de la liste
    $(".mod_button").click(function () {
        // on récupère le type de l'article
        var type = $(this).attr("type");
        var status = $(this).attr("status");

        if (type == "P") {
            if (status == "0") {
                $("#programming").load("prefabs/TNSI/P_tgnsi_big.html");
                $("#programming").css("text-align", "center");
                $(this).attr("status", "1");
            }

            if (status == "1") {
                $("#programming").load("prefabs/TNSI/P_tgnsi_line.html");
                $("#programming").css("text-align", "left");
                $(this).attr("status", "0");
            }
        }

        if (type == "A") {
            if (status == "0") {
                $("#algorithms").load("prefabs/TNSI/A_tgnsi_big.html");
                $("#algorithms").css("text-align", "center");
                $(this).attr("status", "1");
            }

            if (status == "1") {
                $("#algorithms").load("prefabs/TNSI/A_tgnsi_line.html");
                $("#algorithms").css("text-align", "left");
                $(this).attr("status", "0");
            }
        }

        if (type == "BD") {
            if (status == "0") {
                $("#database").load("prefabs/TNSI/BD_tgnsi_big.html");
                $("#database").css("text-align", "center");
                $(this).attr("status", "1");
            }

            if (status == "1") {
                $("#database").load("prefabs/TNSI/BD_tgnsi_line.html");
                $("#database").css("text-align", "left");
                $(this).attr("status", "0");
            }
        }

        if (type == "ARD") {
            if (status == "0") {
                $("#hardware_archi").load("prefabs/TNSI/ARD_tgnsi_big.html");
                $("#hardware_archi").css("text-align", "center");
                $(this).attr("status", "1");
            }

            if (status == "1") {
                $("#hardware_archi").load("prefabs/TNSI/ARD_tgnsi_line.html");
                $("#hardware_archi").css("text-align", "left");
                $(this).attr("status", "0");
            }
        }

        // on change le lien de l'image
        if (status == "1") {
            $(this).find(".mod_image").attr("src", "img/line_mod.png");
        } else {
            $(this).find(".mod_image").attr("src", "img/big_mod.png");
        }

    });

});