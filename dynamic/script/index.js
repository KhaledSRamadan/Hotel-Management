$( function() {
   //********** date piker ***********//
   var dateFormat = "mm/dd/yy",
       from = $( "#arrival-date" )
   .datepicker({

      showOn: "button",
      buttonImage: "layout/images/calendar.gif",
      buttonImageOnly: true,
      buttonText: "Select date",
      defaultDate: "+1w",
      changeMonth: true,
      numberOfMonths: 1
   })
   .on( "change", function() {
      to.datepicker( "option", "minDate", getDate( this ) );
   }),
       to = $( "#leave-date" ).datepicker({

          showOn: "button",
          buttonImage: "layout/images/calendar.gif",
          buttonImageOnly: true,
          buttonText: "Select date",
          defaultDate: "+1w",
          changeMonth: true,
          numberOfMonths: 1
       })
   .on( "change", function() {
      from.datepicker( "option", "maxDate", getDate( this ) );
   });

   function getDate( element ) {
      var date;
      try {
         date = $.datepicker.parseDate( dateFormat, element.value );
      } catch( error ) {
         date = null;
      }

      return date;
   }

   //********** price slider ***********//
   $( "#slider-range" ).slider({
      range: true,
      min: 0,
      max: 1000,
      values: [ 0, 1000 ],
      slide: function( event, ui ) {
         $( "#amount" ).val( "$" + ui.values[ 0 ] + " - $" + ui.values[ 1 ] );
      }
   });
   $( "#amount" ).val( "$" + $( "#slider-range" ).slider( "values", 0 ) + " - $" + $( "#slider-range" ).slider( "values", 1 ) );
   
} );
