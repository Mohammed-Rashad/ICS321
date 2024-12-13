import React, { useState } from 'react';
import { 
  Train, Users, Calendar, Ticket, ListChecks, UserPlus, Shield, UserCog 
} from 'lucide-react';



// Mock data (in a real app, this would come from an API)
const initialTrains = [
  { 
    id: 1, 
    name: 'Express Mumbai', 
    stations: ['Mumbai Central', 'Pune', 'Bangalore'], 
    driver: null,
    engineer: null
  },
  { 
    id: 2, 
    name: 'Coastal Connector', 
    stations: ['Chennai', 'Vizag', 'Kolkata'], 
    driver: null,
    engineer: null
  }
];

const initialStaff = [
  { 
    id: 1, 
    name: 'John Doe', 
    email: 'john.doe@railway.com',
    role: 'Driver',
    salary: 45000 
  },
  { 
    id: 2, 
    name: 'Alice Smith', 
    email: 'alice.smith@railway.com',
    role: 'Engineer',
    salary: 50000 
  }
];

const initialAdmins = [
  {
    id: 1,
    name: 'Railway Super Admin',
    email: 'admin@railway.com',
    salary: 75000
  }
];

const initialPassengers = [
  { 
    id: 1, 
    name: 'Rahul Kumar', 
    trainId: 1, 
    status: 'confirmed',
    seat: '12A'
  },
  { 
    id: 2, 
    name: 'Priya Sharma', 
    trainId: 1, 
    status: 'waitlist',
    seat: null
  }
];

const RailwayDashboard = () => {
  const [trains, setTrains] = useState(initialTrains);
  const [staff, setStaff] = useState(initialStaff);
  const [admins, setAdmins] = useState(initialAdmins);
  const [passengers, setPassengers] = useState(initialPassengers);
  const [activeSection, setActiveSection] = useState('trains');
  
  // New state for form management
  const [isAddStaffModalOpen, setIsAddStaffModalOpen] = useState(false);
  const [isAddAdminModalOpen, setIsAddAdminModalOpen] = useState(false);
  const [newStaffForm, setNewStaffForm] = useState({
    name: '',
    email: '',
    password: '',
    role: 'Driver',
    salary: ''
  });
  const [newAdminForm, setNewAdminForm] = useState({
    name: '',
    email: '',
    password: '',
    salary: ''
  });

  // Previous methods remain the same...

  // New method to handle staff creation
  const createStaff = (e: any) => {
    e.preventDefault();
    const newStaff = {
      ...newStaffForm,
      id: staff.length + 1,
      salary: parseFloat(newStaffForm.salary)
    };
    setStaff([...staff, newStaff]);
    setIsAddStaffModalOpen(false);
    // Reset form
    setNewStaffForm({
      name: '',
      email: '',
      password: '',
      role: 'Driver',
      salary: ''
    });
  };

  // New method to handle admin creation
  const createAdmin = (e: any) => {
    e.preventDefault();
    const newAdmin = {
      ...newAdminForm,
      id: admins.length + 1,
      salary: parseFloat(newAdminForm.salary)
    };
    setAdmins([...admins, newAdmin]);
    setIsAddAdminModalOpen(false);
    // Reset form
    setNewAdminForm({
      name: '',
      email: '',
      password: '',
      salary: ''
    });
  };

  // New method to render staff management section
  const renderStaffSection = () => (
    <div className="p-6">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-2xl font-bold flex items-center">
          <UserCog className="mr-2" /> Staff Management
        </h2>
        <button 
          onClick={() => setIsAddStaffModalOpen(true)}
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 flex items-center"
        >
          <UserPlus className="mr-2" /> Add Staff
        </button>
      </div>

      <table className="w-full bg-white shadow rounded-lg">
        <thead className="bg-gray-100">
          <tr>
            <th className="p-3 text-left">Name</th>
            <th className="p-3 text-left">Email</th>
            <th className="p-3 text-left">Role</th>
            <th className="p-3 text-left">Salary</th>
          </tr>
        </thead>
        <tbody>
          {staff.map(member => (
            <tr key={member.id} className="border-b">
              <td className="p-3">{member.name}</td>
              <td className="p-3">{member.email}</td>
              <td className="p-3">{member.role}</td>
              <td className="p-3">{member.salary.toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* Staff Add Modal */}
      {isAddStaffModalOpen && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
          <div className="bg-white p-6 rounded-lg w-96">
            <h3 className="text-xl font-bold mb-4">Add New Staff</h3>
            <form onSubmit={createStaff}>
              <input 
                type="text" 
                placeholder="Name" 
                required
                value={newStaffForm.name}
                onChange={(e) => setNewStaffForm({...newStaffForm, name: e.target.value})}
                className="w-full border p-2 mb-2 rounded"
              />
              <input 
                type="email" 
                placeholder="Email" 
                required
                value={newStaffForm.email}
                onChange={(e) => setNewStaffForm({...newStaffForm, email: e.target.value})}
                className="w-full border p-2 mb-2 rounded"
              />
              <input 
                type="password" 
                placeholder="Password" 
                required
                value={newStaffForm.password}
                onChange={(e) => setNewStaffForm({...newStaffForm, password: e.target.value})}
                className="w-full border p-2 mb-2 rounded"
              />
              <select
                value={newStaffForm.role}
                onChange={(e) => setNewStaffForm({...newStaffForm, role: e.target.value})}
                className="w-full border p-2 mb-2 rounded"
              >
                <option value="Driver">Driver</option>
                <option value="Engineer">Engineer</option>
              </select>
              <input 
                type="number" 
                placeholder="Salary" 
                required
                value={newStaffForm.salary}
                onChange={(e) => setNewStaffForm({...newStaffForm, salary: e.target.value})}
                className="w-full border p-2 mb-2 rounded"
              />
              <div className="flex justify-end space-x-2">
                <button 
                  type="button"
                  onClick={() => setIsAddStaffModalOpen(false)}
                  className="bg-gray-300 text-black px-4 py-2 rounded"
                >
                  Cancel
                </button>
                <button 
                  type="submit"
                  className="bg-blue-500 text-white px-4 py-2 rounded"
                >
                  Add Staff
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );

  // New method to render admin management section
  const renderAdminSection = () => (
    <div className="p-6">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-2xl font-bold flex items-center">
          <Shield className="mr-2" /> Admin Management
        </h2>
        <button 
          onClick={() => setIsAddAdminModalOpen(true)}
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 flex items-center"
        >
          <UserPlus className="mr-2" /> Add Admin
        </button>
      </div>

      <table className="w-full bg-white shadow rounded-lg">
        <thead className="bg-gray-100">
          <tr>
            <th className="p-3 text-left">Name</th>
            <th className="p-3 text-left">Email</th>
            <th className="p-3 text-left">Salary</th>
          </tr>
        </thead>
        <tbody>
          {admins.map(admin => (
            <tr key={admin.id} className="border-b">
              <td className="p-3">{admin.name}</td>
              <td className="p-3">{admin.email}</td>
              <td className="p-3">{admin.salary.toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* Admin Add Modal */}
      {isAddAdminModalOpen && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
          <div className="bg-white p-6 rounded-lg w-96">
            <h3 className="text-xl font-bold mb-4">Add New Admin</h3>
            <form onSubmit={createAdmin}>
              <input 
                type="text" 
                placeholder="Name" 
                required
                value={newAdminForm.name}
                onChange={(e) => setNewAdminForm({...newAdminForm, name: e.target.value})}
                className="w-full border p-2 mb-2 rounded"
              />
              <input 
                type="email" 
                placeholder="Email" 
                required
                value={newAdminForm.email}
                onChange={(e) => setNewAdminForm({...newAdminForm, email: e.target.value})}
                className="w-full border p-2 mb-2 rounded"
              />
              <input 
                type="password" 
                placeholder="Password" 
                required
                value={newAdminForm.password}
                onChange={(e) => setNewAdminForm({...newAdminForm, password: e.target.value})}
                className="w-full border p-2 mb-2 rounded"
              />
              <input 
                type="number" 
                placeholder="Salary" 
                required
                value={newAdminForm.salary}
                onChange={(e) => setNewAdminForm({...newAdminForm, salary: e.target.value})}
                className="w-full border p-2 mb-2 rounded"
              />
              <div className="flex justify-end space-x-2">
                <button 
                  type="button"
                  onClick={() => setIsAddAdminModalOpen(false)}
                  className="bg-gray-300 text-black px-4 py-2 rounded"
                >
                  Cancel
                </button>
                <button 
                  type="submit"
                  className="bg-blue-500 text-white px-4 py-2 rounded"
                >
                  Add Admin
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
  const renderTrainSection = () => (
    <div className="p-6">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-2xl font-bold flex items-center">
          <Train className="mr-2" /> Train Management
        </h2>
      </div>
  
      <table className="w-full bg-white shadow rounded-lg">
        <thead className="bg-gray-100">
          <tr>
            <th className="p-3 text-left">Train Name</th>
            <th className="p-3 text-left">Stations</th>
            <th className="p-3 text-left">Driver</th>
            <th className="p-3 text-left">Engineer</th>
          </tr>
        </thead>
        <tbody>
          {trains.map(train => (
            <tr key={train.id} className="border-b">
              <td className="p-3">{train.name}</td>
              <td className="p-3">{train.stations.join(', ')}</td>
              <td className="p-3">{train.driver ? train.driver : 'N/A'}</td>
              <td className="p-3">{train.engineer ? train.engineer : 'N/A'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
  
  const renderPassengersSection = () => (
    <div className="p-6">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-2xl font-bold flex items-center">
          <Users className="mr-2" /> Passengers
        </h2>
      </div>
  
      <table className="w-full bg-white shadow rounded-lg">
        <thead className="bg-gray-100">
          <tr>
            <th className="p-3 text-left">Passenger Name</th>
            <th className="p-3 text-left">Train</th>
            <th className="p-3 text-left">Seat</th>
            <th className="p-3 text-left">Status</th>
          </tr>
        </thead>
        <tbody>
          {passengers.map(passenger => {
            const train = trains.find(train => train.id === passenger.trainId);
            return (
              <tr key={passenger.id} className="border-b">
                <td className="p-3">{passenger.name}</td>
                <td className="p-3">{train ? train.name : 'N/A'}</td>
                <td className="p-3">{passenger.seat || 'N/A'}</td>
                <td className="p-3">{passenger.status}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
    </div>
  );
  
  // Update sidebar and content rendering
  return (
    <div className="min-h-screen bg-gray-100 flex">
      {/* Sidebar */}
      <div className="w-64 bg-white shadow-md">
        <div className="p-4 text-2xl font-bold border-b">
          Railway Admin
        </div>
        <nav className="p-4">
          <button 
            onClick={() => setActiveSection('trains')}
            className={`flex items-center w-full p-2 rounded mb-2 ${
              activeSection === 'trains' 
                ? 'bg-blue-500 text-white' 
                : 'hover:bg-gray-200'
            }`}
          >
            <Train className="mr-2" /> Trains
          </button>
          <button 
            onClick={() => setActiveSection('passengers')}
            className={`flex items-center w-full p-2 rounded mb-2 ${
              activeSection === 'passengers' 
                ? 'bg-blue-500 text-white' 
                : 'hover:bg-gray-200'
            }`}
          >
            <Users className="mr-2" /> Passengers
          </button>
          <button 
            onClick={() => setActiveSection('staff')}
            className={`flex items-center w-full p-2 rounded mb-2 ${
              activeSection === 'staff' 
                ? 'bg-blue-500 text-white' 
                : 'hover:bg-gray-200'
            }`}
          >
            <UserCog className="mr-2" /> Staff
          </button>
          <button 
            onClick={() => setActiveSection('admins')}
            className={`flex items-center w-full p-2 rounded ${
              activeSection === 'admins' 
                ? 'bg-blue-500 text-white' 
                : 'hover:bg-gray-200'
            }`}
          >
            <Shield className="mr-2" /> Admins
          </button>
        </nav>
      </div>

      {/* Main Content */}
      <div className="flex-1">
        {activeSection === 'trains' && renderTrainSection()}
        {activeSection === 'passengers' && renderPassengersSection()}
        {activeSection === 'staff' && renderStaffSection()}
        {activeSection === 'admins' && renderAdminSection()}
      </div>
    </div>
  );
};

export default RailwayDashboard;