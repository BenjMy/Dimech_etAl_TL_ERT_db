---
custom_page_title: "A review on applications of time-lapse electrical
resistivity tomography over the last 30 years :
perspectives for mining waste monitoring"
exclude_h1: true
template: table.html
---


<div class="callout">

How to use the table

* filter by collumn
* filter by user input
* export
* add collumns

</div>



<div class="spinner-border text-primary" role="status">
  <span class="sr-only">Loading...</span>
</div>


<section id="TL_ERT_db">
 <div class="container">
   <table id="result-table" class="display" style="width:100%">
  <thead>
      <tr>
	  <th>ID</th>
	  <th>Title</th>	  
  	  <th>Journal</th>
	  <th>Year</th>
	  <th>Type of survey</th>
	  <th>Field of application</th>
      </tr>
  </thead>
  <tbody>
  </tbody>
  </table>
 </div>
</section>


<div class="callout">
Found a typo?
</div>




<script>

function buildTable(db) {
    let fields = ["ID",
		      "Title",
		      "Journal",
		      "Year",
		      "Type of survey",
		      "Field of application"]

    let tbody = document.getElementById('result-table').getElementsByTagName('tbody')[0];

    for (let i = 0; i < db.length; i ++) {
      var tr = tbody.insertRow()
      for (let j = 0; j < fields.length; j ++) {
        let td = tr.insertCell()
        if (fields[j] == "publication_link") {
          td.innerHTML = '<a href="' + db[i]['publication_link'] + '"target="_blank">link</a>'
        } else if (fields[j] == "id") {
          td.innerHTML = '<a href="contribution_details.html?id=' + db[i]['id'] + '">details</a>'
        } else {
          var newText = document.createTextNode(db[i][fields[j]])
          td.appendChild(newText)
        }
      }
    }
    // let table = $('#result-table')
    // table.bootstrapTable();

    // Basic example
    // let oTable = $('#result-table').DataTable();   //pay attention to capital D, which is mandatory to retrieve "api" datatables' object, as @Lionel said
    //  $('#myInputTextField').keyup(function(){
    //        oTable.search($(this).val()).draw() ;
    // })
    //$(document).ready( function () {
      //$('#result-table').bootstrapTable();
      //$('#result-table').DataTable();
      //});



$(document).ready(function() {
    var table = $('#result-table').DataTable( {
        lengthChange: false,
        buttons: [ 'copy', 'excel', 'pdf', 'colvis' ]
    } );
 
    table.buttons().container()
        .insertBefore( '#example_filter' );
} );


    $(document).ready(function() {
	      $('.spinner-border').hide();
	});
      
  }




// loading the database (.csv file)
let dbb = {}

Papa.parse("csv_db.csv", {
  download: true,
  //worker: true,
  header: true,
  //worker: true, // for large csv
  complete: function(res) {
    console.log('database loaded:', res);
    callback(res)
    dbb = res.data
    }
  });
 
  
// main callback function that build interactive elements of the page

function callback(res) {
  let db = res.data

  // setup the interactive table
  buildTable(db)
  console.log('all done')
}

  
  
</script>


