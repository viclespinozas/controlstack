db = db.getSiblingDB('controlstack');

db.createCollection('expenses');
db.expenses.insertMany([
  { category: 'utilities', amount: 120.50, description: 'Electricity', date: new Date() },
  { category: 'streaming', amount: 14.99, description: 'Netflix', date: new Date() },
  { category: 'transport', amount: 45.00, description: 'Gas refill', date: new Date() }
]);
