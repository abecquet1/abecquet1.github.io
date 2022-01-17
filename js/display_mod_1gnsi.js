$(document).ready(function () {

    // chargement de l'affichage par défaut
    $("#programming").load("prefabs/1NSI/P_1gnsi_big.html");
    $("#algorithms").load("prefabs/1NSI/A_1gnsi_big.html");
    $("#table_data").load("prefabs/1NSI/T_1gnsi_big.html");
    $("#hardware_archi").load("prefabs/1NSI/ARD_1gnsi_big.html");
    $("#systems_networks").load("prefabs/1NSI/SR_1gnsi_big.html");

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
    $(".mod_button").click(function () {
        // on récupère le type de l'article
        var type = $(this).attr("type");
        var status = $(this).attr("status");

        if (type == "P") {
            if (status == "0") {
                $("#programming").load("prefabs/1NSI/P_1gnsi_big.html");
                $("#programming").css("text-align", "center");
                $(this).attr("status", "1");
            }

            if (status == "1") {
                $("#programming").load("prefabs/1NSI/P_1gnsi_line.html");
                $("#programming").css("text-align", "left");
                $(this).attr("status", "0");
            }
        }

        if (type == "A") {
            if (status == "0") {
                $("#algorithms").load("prefabs/1NSI/A_1gnsi_big.html");
                $("#algorithms").css("text-align", "center");
                $(this).attr("status", "1");
            }

            if (status == "1") {
                $("#algorithms").load("prefabs/1NSI/A_1gnsi_line.html");
                $("#algorithms").css("text-align", "left");
                $(this).attr("status", "0");
            }
        }

        if (type == "T") {
            if (status == "0") {
                $("#table_data").load("prefabs/1NSI/T_1gnsi_big.html");
                $("#table_data").css("text-align", "center");
                $(this).attr("status", "1");
            }

            if (status == "1") {
                $("#table_data").load("prefabs/1NSI/T_1gnsi_line.html");
                $("#table_data").css("text-align", "left");
                $(this).attr("status", "0");
            }
        }

        if (type == "ARD") {
            if (status == "0") {
                $("#hardware_archi").load("prefabs/1NSI/ARD_1gnsi_big.html");
                $("#hardware_archi").css("text-align", "center");
                $(this).attr("status", "1");
            }

            if (status == "1") {
                $("#hardware_archi").load("prefabs/1NSI/ARD_1gnsi_line.html");
                $("#hardware_archi").css("text-align", "left");
                $(this).attr("status", "0");
            }
        }

        if (type == "SR") {
            if (status == "0") {
                $("#systems_networks").load("prefabs/1NSI/SR_1gnsi_big.html");
                $("#systems_networks").css("text-align", "center");
                $(this).attr("status", "1");
            }

            if (status == "1") {
                $("#systems_networks").load("prefabs/1NSI/SR_1gnsi_line.html");
                $("#systems_networks").css("text-align", "left");
                $(this).attr("status", "0");
            }
        }

    });

});