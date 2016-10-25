Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname> and <nickname>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact
  
  Examples:
  | firstname  | lastname  | nickname |
  | nameesq    | true      | nick123  |
  
  
      
Scenario: Delete a contact
   Given a non-empty contact list
   Given a random contact from the list
   When I delete the contact from the list
   Then the new contact list is equal to the old list without deleted contact
   
Scenario: Modify a contact
   Given a non-empty contact list
   Given a random contact from the list
   When I modify the contact from the list with next contact data <firstname>, <lastname>
   Then list with modified contact list is equal to the old list with not modified contact