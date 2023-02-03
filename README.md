# projet_djaongo

objectif : créer des quiz et les partager à ses amis à l'aide d'un lien 

fonctionnalités : 
- connexion / déconnexion x
- obligé d'être cp pour créer des quiz
- créer des quiz
-> pour chaque quiz, une question et plusieurs réponses 
-> nbre de questions illimité
- générer un lien spécifique à chaque quiz
- pouvoir partager le lien 
- seul celui qui a créé le quiz peut voir le résultat
- pas besoin d'être connecté pour faire le quiz mais on doit rentrer un username
- pourcentage de bonnes réponses affiché

<lié>
	table avec les questions -> user qui a créé ForeignKey
	table avec les réponses -> ManyToOne (table avec les questions)
</lié>

