export class HolbertonClass {
    constructor(year, location) {
      // Initialise les attributs de la classe
      this._year = year;
      this._location = location;
    }
  
    // Récupère l'année
    get year() {
      return this._year;
    }
  
    // Récupère l'emplacement
    get location() {
      return this._location;
    }
  }
  
  export class StudentHolberton {
    constructor(firstName, lastName, holbertonClass) {
      // Initialise les attributs de la classe
      this._firstName = firstName;
      this._lastName = lastName;
      this._holbertonClass = holbertonClass;
    }
  
    // Récupère le nom complet
    get fullName() {
      return `${this._firstName} ${this._lastName}`;
    }
  
    // Récupère la classe Holberton associée
    get holbertonClass() {
      return this._holbertonClass;
    }
  
    // Récupère la description complète
    get fullStudentDescription() {
      return `${this._firstName} ${this._lastName} - ${this._holbertonClass.year} - ${this._holbertonClass.location}`;
    }
  }
  
  // Création d'instances de classes pour 2019 et 2020
  const class2019 = new HolbertonClass(2019, 'San Francisco');
  const class2020 = new HolbertonClass(2020, 'San Francisco');
  
  // Création d'instances d'étudiants avec leurs noms et la classe associée
  const student1 = new StudentHolberton('Guillaume', 'Salva', class2020);
  const student2 = new StudentHolberton('John', 'Doe', class2020);
  const student3 = new StudentHolberton('Albert', 'Clinton', class2019);
  const student4 = new StudentHolberton('Donald', 'Bush', class2019);
  const student5 = new StudentHolberton('Jason', 'Sandler', class2019);
  
  // Liste des étudiants
  export const studentsList = [student1, student2, student3, student4, student5];
  export default [student1, student2, student3, student4, student5];
