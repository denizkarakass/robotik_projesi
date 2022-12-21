const Agents = require('../models/Agents');


exports.AgentStatus = async (req, res) => {
    try {    
  
      const agent = await Agents.findOne({name:req.paramas.name});
      agent.status = req.body.status;
      agent.save();
  
      res.status(200).redirect('/');
  
    } catch (error) {
      res.status(400).json({
        status: 'fail',
        error,
      });
    }
  };

 