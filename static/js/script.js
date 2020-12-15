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
    
    // Floating action button
    $('.fixed-action-btn').floatingActionButton();

    // Tooltip on floating action buttons
    $('.tooltipped').tooltip();

    // Confirm delete modal
    $('.modal').modal();

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

// Function to add another ingredient to add recipe form
$("#add_ingredient").click(function(){
    ingredient = "<div class='input-field col s12 m6'><input type='text' name='recipe_ingredient[]' id='ingredient' class='validate materialize-textarea' minlength='3' required><label for='ingredient'>Ingredient</label><i class='delete_ingredient fas fa-trash-alt delete-button'></i></div>"
    $("#recipe_ingredient_field").append(ingredient)
})

// Function to delete ingredient field when adding or deleting recipes
$("#recipe_ingredient_field").on("click", ".delete_ingredient", function(){ 
    $(this).parent('div').remove(); 
});

// Function to add another method to add recipe form
$("#add_method").click(function(){
    method = "<div class='input-field col s12'><textarea name='recipe_method[]' id='method' class='validate materialize-textarea' minlength='3' required></textarea><label for='method'>Next Step</label><i class=' delete_method fas fa-trash-alt delete-button'></i></div>"
    $("#recipe_method_field").append(method)
})

// Function to delete method field when adding or deleting recipes
$("#recipe_method_field").on("click", ".delete_method", function(){ 
    $(this).parent('div').remove(); 
});

// Rich text editor for creating blog posts
tinymce.init({
  selector: 'textarea#blog_text',
  height: 600,
  placeholder: 'Type blog here...'
});

// Validate user input into rich-text editor for adding a blog
$("#blog_submit").click(function(){
    var blogText = tinymce.get("blog_text").getContent();
    if(blogText.length == 0){
        event.preventDefault()
        $('.blog_editor').css("border", "1px solid #f44336")
        alert("Blog text area cannot be empty!")
    }
});

// Image replacement for any broken image links 
$('img').on("error", function() {
  $(this).attr('src', 'https://images.unsplash.com/reserve/EnF7DhHROS8OMEp2pCkx_Dufer%20food%20overhead%20hig%20res.jpg?ixlib=rb-1.2.1&ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&auto=format&fit=crop&w=1514&q=80');
});