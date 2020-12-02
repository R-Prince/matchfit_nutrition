$(document).ready(function(){
    // Mobile Navbar
    $('.sidenav').sidenav();

    // Add Recipes - Select difficulty
    $('select').formSelect();

    // Date Picker for blog form
    $('.datepicker').datepicker({
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });
    // Validate Add Recipe materialize form (Copied from Code Institute - Materialize Form Validation)
    validateMaterializeSelect();
    function validateMaterializeSelect() {
        let classValid = { "border-bottom": "1px solid #4caf50", "box-shadow": "0 1px 0 0 #4caf50" };
        let classInvalid = { "border-bottom": "1px solid #f44336", "box-shadow": "0 1px 0 0 #f44336" };
        if ($("select.validate").prop("required")) {
            $("select.validate").css({ "display": "block", "height": "0", "padding": "0", "width": "0", "position": "absolute" });
        }
        $(".select-wrapper input.select-dropdown").on("focusin", function () {
            $(this).parent(".select-wrapper").on("change", function () {
                if ($(this).children("ul").children("li.selected:not(.disabled)").on("click", function () { })) {
                    $(this).children("input").css(classValid);
                }
            });
        }).on("click", function () {
            if ($(this).parent(".select-wrapper").children("ul").children("li.selected:not(.disabled)").css("background-color") === "rgba(0, 0, 0, 0.03)") {
                $(this).parent(".select-wrapper").children("input").css(classValid);
            } else {
                $(".select-wrapper input.select-dropdown").on("focusout", function () {
                    if ($(this).parent(".select-wrapper").children("select").prop("required")) {
                        if ($(this).css("border-bottom") != "1px solid rgb(76, 175, 80)") {
                            $(this).parent(".select-wrapper").children("input").css(classInvalid);
                        }
                    }
                });
            }
        });
    }
});

// Function to add another ingredient to recipe
$("#add_ingredient").click(function(){
    ingredient = "<div class='input-field col s6'><input id='recipe_ingredient' type='text' name='recipe_ingredient[]' class='validate materialize-textarea' minlength='3' required><label for='recipe_ingredient'>Ingredient</label><i id='delete_ingredient' class='fas fa-trash-alt delete-button'></i></div>"
    $("#recipe_ingredient_field").append(ingredient)
})

// Function to delete ingredient field when adding or deleting recipes
$("#recipe_ingredient_field").on("click", "#delete_ingredient", function(){ 
    $(this).parent('div').remove(); 
});

// Function to add another method to recipe
$("#add_method").click(function(){
    method = "<div class='input-field col s12'><textarea id='recipe_method' type='text' name='recipe_method[]' class='validate materialize-textarea' minlength='3' required></textarea><label for='recipe_method'>Recipe Method</label><i id='delete_method' class='fas fa-trash-alt delete-button'></i></div>"
    $("#recipe_method_field").append(method)
})

// Function to delete method field when adding or deleting recipes
$("#recipe_method_field").on("click", "#delete_method", function(){ 
    $(this).parent('div').remove(); 
});
