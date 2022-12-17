
const Agents = require('../models/Agents');

exports.getIndexPage = async(req, res) => {
    console.log(req.session.userID);
    const agents = await Agents.find();
    res.status(200).render('index', {
        agents
    });
  }