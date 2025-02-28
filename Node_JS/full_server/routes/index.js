import { AppController } from "../controllers/AppController";
import { StudentsController } from "../controllers/StudentsController";
const express = require('express');
const routes = express.Router();

routes.get('/', AppController.getHomepage);

routes.get('/students', StudentsController.getAllStudents);
routes.get('/students/:major', StudentsController.getAllStudentsByMajor);

module.exports = routes;