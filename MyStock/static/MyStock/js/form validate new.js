<script type="text/javascript">

  //Find the values added in form using the id of each fields. The ".val()" function finds the value added in the form fields.
  var Category Id = $('#Category Id').val();
  var Category Name = $('#Category Name').val();
 
  
  //Function will execute when the button "Click to Submit" is clicked.
  $('#btnvalidate').click(function() {
	  
    //Blank field validation of fullname, mobile no and address. The function will generate an alert message if "fullname" or "mobile no" or "address" field is blank  
    if( Category Id== '')
    {
	  alert('Please enter Category Id');
	  $('#Category Id').focus(); //The focus function will move the cursor to "fullname" field
    }
    else if(Category Name == '')
    {
	  alert('Please enter Category Name');
	  $('#Category Name').focus();
    }
   
  });
  
</script>