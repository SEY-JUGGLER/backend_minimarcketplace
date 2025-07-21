/***********************************************************************
 * Module:  Anonce.java
 * Author:  EL hadji Mor Seye
 * Purpose: Defines the Class Anonce
 ***********************************************************************/

import java.util.*;

/** @pdOid cf2f6f7a-7758-436a-a07c-bc8a9490e4f3 */
public class Anonce {
   /** @pdOid ca9794e1-6559-4b50-a342-4de328da6dd9 */
   public int idAnonce;
   /** @pdOid e69c7df1-093d-4696-adc5-06c41995a946 */
   public java.lang.String titre;
   /** @pdOid 371f113e-d385-4003-b9c7-100eee31ea56 */
   public java.lang.String description;
   /** @pdOid dbd8ec37-c8de-4dfc-b72a-3c89f2a15a46 */
   public double prix;
   /** @pdOid fc2840af-12d6-40e6-8ac8-2da9345c7e01 */
   public java.util.Date dateDePublication;
   /** @pdOid dea4433b-1a82-4d44-929b-cd5587aa5e8e */
   public java.lang.String imageUrl;
   
   /** @pdRoleInfo migr=no name=Message assc=concerne coll=java.util.Collection impl=java.util.HashSet mult=0..* side=A */
   public java.util.Collection<Message> message;
   
   
   /** @pdGenerated default getter */
   public java.util.Collection<Message> getMessage() {
      if (message == null)
         message = new java.util.HashSet<Message>();
      return message;
   }
   
   /** @pdGenerated default iterator getter */
   public java.util.Iterator getIteratorMessage() {
      if (message == null)
         message = new java.util.HashSet<Message>();
      return message.iterator();
   }
   
   /** @pdGenerated default setter
     * @param newMessage */
   public void setMessage(java.util.Collection<Message> newMessage) {
      removeAllMessage();
      for (java.util.Iterator iter = newMessage.iterator(); iter.hasNext();)
         addMessage((Message)iter.next());
   }
   
   /** @pdGenerated default add
     * @param newMessage */
   public void addMessage(Message newMessage) {
      if (newMessage == null)
         return;
      if (this.message == null)
         this.message = new java.util.HashSet<Message>();
      if (!this.message.contains(newMessage))
         this.message.add(newMessage);
   }
   
   /** @pdGenerated default remove
     * @param oldMessage */
   public void removeMessage(Message oldMessage) {
      if (oldMessage == null)
         return;
      if (this.message != null)
         if (this.message.contains(oldMessage))
            this.message.remove(oldMessage);
   }
   
   /** @pdGenerated default removeAll */
   public void removeAllMessage() {
      if (message != null)
         message.clear();
   }

}