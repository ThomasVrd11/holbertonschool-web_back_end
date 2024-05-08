/* 1-make_classrooms */
import ClassRoom from './0-classroom';

function initializeRooms() {
  /* Créez un array d'objets ClassRoom avec les size spécifiées */
  const rooms = [
    new ClassRoom(19),
    new ClassRoom(20),
    new ClassRoom(34),
  ];

  return rooms;
}

export default initializeRooms;
