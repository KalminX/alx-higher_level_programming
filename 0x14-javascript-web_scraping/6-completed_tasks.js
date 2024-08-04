#!/usr/bin/node

const { argv } = require('node:process');
const request = require('request');
const fs = require('fs');

request(argv[2], function (error, response, body) {
  if (error) {
    console.log('error:', error);
    return;
  }
  let tasks = JSON.parse(body);
    try {
      tasks = JSON.parse(body);
    } catch (e) {
      console.log("Invalid JSON:", e);
      return;
    }

  const completedTasks = tasks.filter(x => x.completed === true);
  let tasksCount = {};
  completedTasks.forEach(x => {
        const userId = x.userId;
        if (!(userId in tasksCount)) {
            tasksCount[userId] = 0;
        } else {
            tasksCount[userId]+=1; 
        }
    })
    console.log(tasksCount);;
  })
