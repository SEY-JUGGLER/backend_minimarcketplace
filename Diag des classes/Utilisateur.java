/***********************************************************************
 * Module:  Utilisateur.java
 * Author:  EL hadji Mor Seye
 * Purpose: Defines the Class Utilisateur
 ***********************************************************************/

import java.util.*;

/** @pdOid ec83bc22-d1db-4aee-aa0f-e46254e5f2e1 */
public class Utilisateur {
   /** @pdOid cc70adf6-c536-49b9-8a13-780be76cce23 */
   public int idUtilisateur;
   /** @pdOid 353fc606-c870-44a0-8166-47b76186d205 */
   public java.lang.String nom;
   /** @pdOid eaa02e05-b38d-4d8f-9861-68e5a15e7b05 */
   public java.lang.String email;
   /** @pdOid db926dcc-5917-4d7c-9609-b247eb1682d6 */
   public java.lang.String motDePasse;
   /** @pdOid 562f8b2f-7d9f-4588-b152-29ab58bf1e06 */
   public java.lang.String role;
   
   /** @pdRoleInfo migr=no name=Anonce assc=publier coll=java.util.Collection impl=java.util.HashSet mult=0..* side=A */
   public java.util.Collection<Anonce> anonce;
   /** @pdRoleInfo migr=no name=Message assc=envoyer coll=java.util.Collection impl=java.util.HashSet mult=0..* side=A */
   public java.util.Collection<Message> message;
   
   
   /** @pdGenerated default getter */
   public java.util.Collection<Anonce> getAnonce() {
      if (anonce == null)
         anonce = new java.util.HashSet<Anonce>();
      return anonce;
   }
   
   /** @pdGenerated default iterator getter */
   public java.util.Iterator getIteratorAnonce() {
      if (anonce == null)
         anonce = new java.util.HashSet<Anonce>();
      return anonce.iterator();
   }
   
   /** @pdGenerated default setter
     * @param newAnonce */
   public void setAnonce(java.util.Collection<Anonce> newAnonce) {
      removeAllAnonce();
      for (java.util.Iterator iter = newAnonce.iterator(); iter.hasNext();)
         addAnonce((Anonce)iter.next());
   }
   
   /** @pdGenerated default add
     * @param newAnonce */
   public void addAnonce(Anonce newAnonce) {
      if (newAnonce == null)
         return;
      if (this.anonce == null)
         this.anonce = new java.util.HashSet<Anonce>();
      if (!this.anonce.contains(newAnonce))
         this.anonce.add(newAnonce);
   }
   
   /** @pdGenerated default remove
     * @param oldAnonce */
   public void removeAnonce(Anonce oldAnonce) {
      if (oldAnonce == null)
         return;
      if (this.anonce != null)
         if (this.anonce.contains(oldAnonce))
            this.anonce.remove(oldAnonce);
   }
   
   /** @pdGenerated default removeAll */
   public void removeAllAnonce() {
      if (anonce != null)
         anonce.clear();
   }
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