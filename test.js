const express = require('express');
const mysql = require('mysql2');

const app = express();
const port = 3000;

// MySQL connection configuration
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'your_username',
  password: 'your_password',
  database: 'todo_db'
});

// Connect to MySQL
connection.connect((err) => {
  if (err) throw err;
  console.log('Connected to MySQL database!');
});

// Middleware
app.use(express.json());

// Create a new todo
app.post('/todos', (req, res) => {
  const { task } = req.body;
  const query = `INSERT INTO todos (task, completed) VALUES (?, false)`;
  connection.query(query, [task], (err, result) => {
    if (err) throw err;
    res.json({ message: 'Todo created!', id: result.insertId });
  });
});

// Get all todos
app.get('/todos', (req, res) => {
  const query = `SELECT * FROM todos`;
  connection.query(query, (err, results) => {
    if (err) throw err;
    res.json(results);
  });
});

// Update a todo
app.put('/todos/:id', (req, res) => {
  const { task, completed } = req.body;
  const query = `UPDATE todos SET task = ?, completed = ? WHERE id = ?`;
  connection.query(query, [task, completed, req.params.id], (err, result) => {
    if (err) throw err;
    res.json({ message: 'Todo updated!' });
  });
});

// Delete a todo
app.delete('/todos/:id', (req, res) => {
  const query = `DELETE FROM todos WHERE id = ?`;
  connection.query(query, [req.params.id], (err, result) => {
    if (err) throw err;
    res.json({ message: 'Todo deleted!' });
  });
});

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
