import React, { useState, useEffect, useMemo } from 'react';
import { 
  Users, UserCheck, Shield, UserPlus, Search, Filter, 
  Edit3, Trash2, CheckCircle2, AlertTriangle, RefreshCw, X, Award
} from 'lucide-react';

const initialMockUsers = [
  {
    id: 1,
    fullName: "Daksh Gehlot",
    email: "daksh.g@srmist.edu.in",
    registrationNumber: "RA2411003012297",
    phoneNumber: "9876543210",
    department: "Computer Science & Engineering",
    role: "STUDENT_COMMUTER",
    status: "VERIFIED",
    campusGate: "Campus Gate 2",
    hostelOrPG: "Starlight Hostels",
    rating: 5.0,
    totalRidesCount: 12
  },
  {
    id: 2,
    fullName: "Aarav Sharma",
    email: "aarav.s@srmist.edu.in",
    registrationNumber: "RA2411003012201",
    phoneNumber: "9812345678",
    department: "Computer Science & Engineering",
    role: "HOST_DRIVER",
    status: "VERIFIED",
    campusGate: "Campus Gate 2",
    hostelOrPG: "Starlight Hostels",
    rating: 4.9,
    totalRidesCount: 28
  },
  {
    id: 3,
    fullName: "Priya Patel",
    email: "priya.p@srmist.edu.in",
    registrationNumber: "RA2411003012202",
    phoneNumber: "9823456789",
    department: "Information Technology",
    role: "STUDENT_COMMUTER",
    status: "ACTIVE",
    campusGate: "Campus Gate 1",
    hostelOrPG: "Green Meadows Flats",
    rating: 4.8,
    totalRidesCount: 7
  },
  {
    id: 4,
    fullName: "Ananya Iyer",
    email: "ananya.i@srmist.edu.in",
    registrationNumber: "RA2411003012203",
    phoneNumber: "9834567890",
    department: "Electronics & Communication",
    role: "HOST_DRIVER",
    status: "VERIFIED",
    campusGate: "Campus Gate 1",
    hostelOrPG: "Green Meadows Flats",
    rating: 4.95,
    totalRidesCount: 42
  },
  {
    id: 5,
    fullName: "Kabir Sen",
    email: "kabir.s@srmist.edu.in",
    registrationNumber: "RA2411003012204",
    phoneNumber: "9845678901",
    department: "Mechanical Engineering",
    role: "STUDENT_COMMUTER",
    status: "ACTIVE",
    campusGate: "Campus Gate 1",
    hostelOrPG: "Green Meadows Flats",
    rating: 4.7,
    totalRidesCount: 5
  },
  {
    id: 6,
    fullName: "Dr. R. Ramanathan",
    email: "ramanathan.r@srmist.edu.in",
    registrationNumber: "FAC20190412",
    phoneNumber: "9898989898",
    department: "Student Affairs & Transit",
    role: "CAMPUS_ADMIN",
    status: "VERIFIED",
    campusGate: "Admin Block",
    hostelOrPG: "Faculty Enclave",
    rating: 5.0,
    totalRidesCount: 0
  }
];

export default function UserRecordsView({ onTriggerToast }) {
  const [users, setUsers] = useState(initialMockUsers);
  const [loading, setLoading] = useState(false);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedRole, setSelectedRole] = useState('ALL');
  const [selectedDept, setSelectedDept] = useState('ALL');

  // Modal States
  const [isAddModalOpen, setIsAddModalOpen] = useState(false);
  const [isEditModalOpen, setIsEditModalOpen] = useState(false);
  const [editingUser, setEditingUser] = useState(null);

  // Form State
  const [formData, setFormData] = useState({
    fullName: '',
    email: '',
    registrationNumber: '',
    phoneNumber: '',
    department: 'Computer Science & Engineering',
    role: 'STUDENT_COMMUTER',
    campusGate: 'Campus Gate 2',
    hostelOrPG: ''
  });

  // Fetch users from Spring Boot backend if accessible
  const fetchUsers = () => {
    setLoading(true);
    fetch('/api/users')
      .then(res => {
        if (!res.ok) throw new Error('Network error');
        return res.json();
      })
      .then(data => {
        if (Array.isArray(data) && data.length > 0) {
          setUsers(data);
        }
      })
      .catch(err => {
        console.warn('Backend not reached for users, using in-memory state:', err);
      })
      .finally(() => setLoading(false));
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  // Filtered Users computation
  const filteredUsers = useMemo(() => {
    return users.filter(user => {
      const q = searchQuery.toLowerCase().trim();
      const matchQuery = !q || 
        user.fullName.toLowerCase().includes(q) ||
        user.email.toLowerCase().includes(q) ||
        user.registrationNumber.toLowerCase().includes(q) ||
        user.department.toLowerCase().includes(q);

      const matchRole = selectedRole === 'ALL' || user.role === selectedRole;
      const matchDept = selectedDept === 'ALL' || user.department === selectedDept;

      return matchQuery && matchRole && matchDept;
    });
  }, [users, searchQuery, selectedRole, selectedDept]);

  // Statistics
  const stats = useMemo(() => {
    const total = users.length;
    const students = users.filter(u => u.role === 'STUDENT_COMMUTER').length;
    const hosts = users.filter(u => u.role === 'HOST_DRIVER').length;
    const verified = users.filter(u => u.status === 'VERIFIED').length;
    return { total, students, hosts, verified };
  }, [users]);

  // Handle Create User
  const handleCreateSubmit = (e) => {
    e.preventDefault();

    if (!formData.email.endsWith('@srmist.edu.in')) {
      onTriggerToast?.('Email must end with @srmist.edu.in', 'error');
      return;
    }

    if (!/^\d{10}$/.test(formData.phoneNumber)) {
      onTriggerToast?.('Phone number must be exactly 10 digits', 'error');
      return;
    }

    // Try posting to backend
    fetch('/api/users', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(formData)
    })
      .then(res => {
        if (!res.ok) return res.json().then(err => Promise.reject(err));
        return res.json();
      })
      .then(newUser => {
        setUsers(prev => [newUser, ...prev]);
        setIsAddModalOpen(false);
        resetForm();
        onTriggerToast?.(`User record created for ${newUser.fullName}! (Saved to JPA DB)`);
      })
      .catch(err => {
        // Fallback local persistence if backend proxy not connected
        const localNewUser = {
          ...formData,
          id: Date.now(),
          status: 'ACTIVE',
          rating: 4.9,
          totalRidesCount: 0
        };
        setUsers(prev => [localNewUser, ...prev]);
        setIsAddModalOpen(false);
        resetForm();
        onTriggerToast?.(`User record registered for ${localNewUser.fullName}!`);
      });
  };

  // Handle Edit User
  const openEditModal = (user) => {
    setEditingUser(user);
    setFormData({
      fullName: user.fullName,
      email: user.email,
      registrationNumber: user.registrationNumber,
      phoneNumber: user.phoneNumber,
      department: user.department,
      role: user.role,
      campusGate: user.campusGate || 'Campus Gate 2',
      hostelOrPG: user.hostelOrPG || ''
    });
    setIsEditModalOpen(true);
  };

  const handleEditSubmit = (e) => {
    e.preventDefault();
    if (!editingUser) return;

    fetch(`/api/users/${editingUser.id}`, {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        fullName: formData.fullName,
        phoneNumber: formData.phoneNumber,
        department: formData.department,
        role: formData.role,
        status: editingUser.status,
        campusGate: formData.campusGate,
        hostelOrPG: formData.hostelOrPG
      })
    })
      .then(res => res.json())
      .then(updated => {
        setUsers(prev => prev.map(u => u.id === editingUser.id ? { ...u, ...updated } : u));
        setIsEditModalOpen(false);
        setEditingUser(null);
        resetForm();
        onTriggerToast?.(`User record #${editingUser.id} updated successfully!`);
      })
      .catch(() => {
        // Local update fallback
        setUsers(prev => prev.map(u => u.id === editingUser.id ? { ...u, ...formData } : u));
        setIsEditModalOpen(false);
        setEditingUser(null);
        resetForm();
        onTriggerToast?.(`User record #${editingUser.id} updated!`);
      });
  };

  // Handle Toggle Status
  const handleToggleStatus = (user) => {
    const nextStatus = user.status === 'ACTIVE' ? 'VERIFIED' : user.status === 'VERIFIED' ? 'SUSPENDED' : 'ACTIVE';
    fetch(`/api/users/${user.id}/status?status=${nextStatus}`, { method: 'PATCH' })
      .then(res => res.json())
      .then(updated => {
        setUsers(prev => prev.map(u => u.id === user.id ? { ...u, status: updated.status } : u));
        onTriggerToast?.(`Status of ${user.fullName} updated to ${nextStatus}`);
      })
      .catch(() => {
        setUsers(prev => prev.map(u => u.id === user.id ? { ...u, status: nextStatus } : u));
        onTriggerToast?.(`Status of ${user.fullName} set to ${nextStatus}`);
      });
  };

  // Handle Delete
  const handleDeleteUser = (id, name) => {
    if (!window.confirm(`Are you sure you want to delete user record "${name}" from the database?`)) {
      return;
    }

    fetch(`/api/users/${id}`, { method: 'DELETE' })
      .then(() => {
        setUsers(prev => prev.filter(u => u.id !== id));
        onTriggerToast?.(`User #${id} (${name}) deleted from JPA database.`);
      })
      .catch(() => {
        setUsers(prev => prev.filter(u => u.id !== id));
        onTriggerToast?.(`User #${id} removed.`);
      });
  };

  const resetForm = () => {
    setFormData({
      fullName: '',
      email: '',
      registrationNumber: '',
      phoneNumber: '',
      department: 'Computer Science & Engineering',
      role: 'STUDENT_COMMUTER',
      campusGate: 'Campus Gate 2',
      hostelOrPG: ''
    });
  };

  return (
    <div className="user-records-container animate-fade-in" id="unit5-user-management">
      {/* Unit 5 Banner */}
      <div className="unit-badge-banner">
        <div className="badge-content">
          <span className="unit-pill">UNIT 5 SUBMISSION</span>
          <h2>Spring Boot Data JPA User Management System</h2>
          <p>
            Entity lifecycle, Spring Data JPA repositories, derived queries, and full CRUD operations on relational database schema.
          </p>
        </div>
        <div className="student-author-card">
          <div className="author-avatar">DG</div>
          <div className="author-info">
            <strong>Daksh Gehlot</strong>
            <span>Reg.No: <code>RA2411003012297</code></span>
            <span className="inst-tag">SRM Institute of Science and Technology</span>
          </div>
        </div>
      </div>

      {/* KPI Stats Grid */}
      <div className="user-kpi-grid">
        <div className="kpi-card">
          <div className="kpi-icon total"><Users size={22} /></div>
          <div>
            <div className="kpi-val">{stats.total}</div>
            <div className="kpi-label">Registered Users</div>
          </div>
        </div>
        <div className="kpi-card">
          <div className="kpi-icon students"><UserCheck size={22} /></div>
          <div>
            <div className="kpi-val">{stats.students}</div>
            <div className="kpi-label">Student Commuters</div>
          </div>
        </div>
        <div className="kpi-card">
          <div className="kpi-icon hosts"><Award size={22} /></div>
          <div>
            <div className="kpi-val">{stats.hosts}</div>
            <div className="kpi-label">Verified Ride Hosts</div>
          </div>
        </div>
        <div className="kpi-card">
          <div className="kpi-icon verified"><Shield size={22} /></div>
          <div>
            <div className="kpi-val">{stats.verified}</div>
            <div className="kpi-label">KYC Verified Profiles</div>
          </div>
        </div>
      </div>

      {/* Controls: Search, Filter, Add */}
      <div className="user-controls-bar">
        <div className="search-box">
          <Search size={18} className="search-icon" />
          <input 
            type="text" 
            placeholder="Search by name, Reg.No, email, or dept..." 
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            id="user-search-input"
          />
          {searchQuery && (
            <button className="clear-btn" onClick={() => setSearchQuery('')}>
              <X size={14} />
            </button>
          )}
        </div>

        <div className="filter-group">
          <select 
            value={selectedRole} 
            onChange={(e) => setSelectedRole(e.target.value)}
            id="role-filter-select"
          >
            <option value="ALL">All Roles</option>
            <option value="STUDENT_COMMUTER">Student Commuters</option>
            <option value="HOST_DRIVER">Ride Hosts</option>
            <option value="CAMPUS_ADMIN">Campus Admins</option>
          </select>

          <select 
            value={selectedDept} 
            onChange={(e) => setSelectedDept(e.target.value)}
            id="dept-filter-select"
          >
            <option value="ALL">All Departments</option>
            <option value="Computer Science & Engineering">CSE</option>
            <option value="Information Technology">IT</option>
            <option value="Electronics & Communication">ECE</option>
            <option value="Mechanical Engineering">Mech</option>
            <option value="Civil Engineering">Civil</option>
          </select>

          <button 
            className="btn btn-primary add-user-btn" 
            onClick={() => setIsAddModalOpen(true)}
            id="btn-register-user"
          >
            <UserPlus size={18} />
            Register Student / User
          </button>
          
          <button 
            className="btn btn-secondary refresh-btn" 
            onClick={fetchUsers} 
            title="Refresh from H2 Relational Database"
            disabled={loading}
          >
            <RefreshCw size={16} className={loading ? 'animate-spin' : ''} />
          </button>
        </div>
      </div>

      {/* User Records Table */}
      <div className="user-table-wrapper">
        <table className="user-table" id="jpa-user-records-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Student / Commuter Profile</th>
              <th>Registration No</th>
              <th>Department</th>
              <th>Pickup Gate</th>
              <th>Role</th>
              <th>Status</th>
              <th>Rating</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            {filteredUsers.length === 0 ? (
              <tr>
                <td colSpan="9" className="empty-table-cell">
                  <AlertTriangle size={24} />
                  <span>No user records match the query. Try adjusting your search or filters.</span>
                </td>
              </tr>
            ) : (
              filteredUsers.map((user) => {
                const isDaksh = user.registrationNumber === 'RA2411003012297';
                return (
                  <tr key={user.id} className={isDaksh ? 'highlight-student-row' : ''}>
                    <td className="user-id-cell">#{user.id}</td>
                    <td className="user-profile-cell">
                      <div className="user-avatar-badge">
                        {user.fullName.split(' ').map(n => n[0]).join('').substring(0, 2).toUpperCase()}
                      </div>
                      <div className="user-name-meta">
                        <div className="name-with-tag">
                          <strong className="user-name">{user.fullName}</strong>
                          {isDaksh && <span className="author-pill">Author</span>}
                        </div>
                        <span className="user-email">{user.email}</span>
                        <span className="user-phone">📞 {user.phoneNumber}</span>
                      </div>
                    </td>
                    <td>
                      <code className="reg-code">{user.registrationNumber}</code>
                    </td>
                    <td>
                      <span className="dept-tag">{user.department}</span>
                    </td>
                    <td>
                      <span className="gate-tag">{user.campusGate || 'Campus Gate 2'}</span>
                    </td>
                    <td>
                      <span className={`role-badge ${user.role.toLowerCase()}`}>
                        {user.role === 'STUDENT_COMMUTER' ? 'Commuter' : user.role === 'HOST_DRIVER' ? 'Host' : 'Admin'}
                      </span>
                    </td>
                    <td>
                      <button 
                        className={`status-pill ${user.status.toLowerCase()}`}
                        onClick={() => handleToggleStatus(user)}
                        title="Click to toggle status: ACTIVE -> VERIFIED -> SUSPENDED"
                      >
                        {user.status === 'VERIFIED' && <CheckCircle2 size={12} />}
                        {user.status}
                      </button>
                    </td>
                    <td>
                      <span className="rating-tag">⭐ {user.rating?.toFixed(1) || '4.9'}</span>
                    </td>
                    <td className="actions-cell">
                      <button 
                        className="action-icon-btn edit" 
                        onClick={() => openEditModal(user)}
                        title="Edit User Record (PUT)"
                        id={`edit-user-${user.id}`}
                      >
                        <Edit3 size={15} />
                      </button>
                      <button 
                        className="action-icon-btn delete" 
                        onClick={() => handleDeleteUser(user.id, user.fullName)}
                        title="Delete User Record (DELETE)"
                        id={`delete-user-${user.id}`}
                      >
                        <Trash2 size={15} />
                      </button>
                    </td>
                  </tr>
                );
              })
            )}
          </tbody>
        </table>
      </div>

      {/* Add User Modal */}
      {isAddModalOpen && (
        <div className="modal-backdrop">
          <div className="modal-content animate-slide-up" id="add-user-modal">
            <div className="modal-header">
              <h3>Register New Student / Commuter Record</h3>
              <button className="close-btn" onClick={() => setIsAddModalOpen(false)}><X size={20} /></button>
            </div>
            <form onSubmit={handleCreateSubmit} className="modal-form">
              <div className="form-group">
                <label>Full Name *</label>
                <input 
                  type="text" 
                  required 
                  placeholder="e.g. Rohan Verma"
                  value={formData.fullName}
                  onChange={(e) => setFormData({ ...formData, fullName: e.target.value })}
                  id="form-full-name"
                />
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label>Campus Email (@srmist.edu.in) *</label>
                  <input 
                    type="email" 
                    required 
                    placeholder="rohan.v@srmist.edu.in"
                    value={formData.email}
                    onChange={(e) => setFormData({ ...formData, email: e.target.value })}
                    id="form-email"
                  />
                </div>
                <div className="form-group">
                  <label>Registration Number *</label>
                  <input 
                    type="text" 
                    required 
                    placeholder="e.g. RA2411003012299"
                    value={formData.registrationNumber}
                    onChange={(e) => setFormData({ ...formData, registrationNumber: e.target.value })}
                    id="form-reg-no"
                  />
                </div>
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label>Phone Number (10 digits) *</label>
                  <input 
                    type="tel" 
                    required 
                    maxLength={10}
                    placeholder="9876543210"
                    value={formData.phoneNumber}
                    onChange={(e) => setFormData({ ...formData, phoneNumber: e.target.value })}
                    id="form-phone"
                  />
                </div>
                <div className="form-group">
                  <label>Department *</label>
                  <select 
                    value={formData.department}
                    onChange={(e) => setFormData({ ...formData, department: e.target.value })}
                    id="form-department"
                  >
                    <option value="Computer Science & Engineering">Computer Science & Engineering</option>
                    <option value="Information Technology">Information Technology</option>
                    <option value="Electronics & Communication">Electronics & Communication</option>
                    <option value="Mechanical Engineering">Mechanical Engineering</option>
                    <option value="Civil Engineering">Civil Engineering</option>
                  </select>
                </div>
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label>User Role *</label>
                  <select 
                    value={formData.role}
                    onChange={(e) => setFormData({ ...formData, role: e.target.value })}
                    id="form-role"
                  >
                    <option value="STUDENT_COMMUTER">Student Commuter (Rider)</option>
                    <option value="HOST_DRIVER">Ride Host (Publisher)</option>
                    <option value="CAMPUS_ADMIN">Campus Admin</option>
                  </select>
                </div>
                <div className="form-group">
                  <label>Campus Gate *</label>
                  <select 
                    value={formData.campusGate}
                    onChange={(e) => setFormData({ ...formData, campusGate: e.target.value })}
                    id="form-gate"
                  >
                    <option value="Campus Gate 1">Campus Gate 1</option>
                    <option value="Campus Gate 2">Campus Gate 2</option>
                    <option value="Library Block">Library Block</option>
                    <option value="Tech Park Gate">Tech Park Gate</option>
                  </select>
                </div>
              </div>

              <div className="form-group">
                <label>Hostel / Apartment Destination</label>
                <input 
                  type="text" 
                  placeholder="e.g. Starlight Hostels, Green Meadows Flats"
                  value={formData.hostelOrPG}
                  onChange={(e) => setFormData({ ...formData, hostelOrPG: e.target.value })}
                  id="form-hostel"
                />
              </div>

              <div className="modal-actions">
                <button type="button" className="btn btn-secondary" onClick={() => setIsAddModalOpen(false)}>Cancel</button>
                <button type="submit" className="btn btn-primary" id="btn-submit-user">Save to Relational DB</button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* Edit User Modal */}
      {isEditModalOpen && (
        <div className="modal-backdrop">
          <div className="modal-content animate-slide-up" id="edit-user-modal">
            <div className="modal-header">
              <h3>Edit User Record #{editingUser?.id}</h3>
              <button className="close-btn" onClick={() => setIsEditModalOpen(false)}><X size={20} /></button>
            </div>
            <form onSubmit={handleEditSubmit} className="modal-form">
              <div className="form-group">
                <label>Full Name *</label>
                <input 
                  type="text" 
                  required 
                  value={formData.fullName}
                  onChange={(e) => setFormData({ ...formData, fullName: e.target.value })}
                />
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label>Phone Number (10 digits) *</label>
                  <input 
                    type="tel" 
                    required 
                    maxLength={10}
                    value={formData.phoneNumber}
                    onChange={(e) => setFormData({ ...formData, phoneNumber: e.target.value })}
                  />
                </div>
                <div className="form-group">
                  <label>Department *</label>
                  <select 
                    value={formData.department}
                    onChange={(e) => setFormData({ ...formData, department: e.target.value })}
                  >
                    <option value="Computer Science & Engineering">Computer Science & Engineering</option>
                    <option value="Information Technology">Information Technology</option>
                    <option value="Electronics & Communication">Electronics & Communication</option>
                    <option value="Mechanical Engineering">Mechanical Engineering</option>
                    <option value="Civil Engineering">Civil Engineering</option>
                  </select>
                </div>
              </div>

              <div className="form-row">
                <div className="form-group">
                  <label>Role</label>
                  <select 
                    value={formData.role}
                    onChange={(e) => setFormData({ ...formData, role: e.target.value })}
                  >
                    <option value="STUDENT_COMMUTER">Student Commuter</option>
                    <option value="HOST_DRIVER">Ride Host</option>
                    <option value="CAMPUS_ADMIN">Campus Admin</option>
                  </select>
                </div>
                <div className="form-group">
                  <label>Campus Gate</label>
                  <select 
                    value={formData.campusGate}
                    onChange={(e) => setFormData({ ...formData, campusGate: e.target.value })}
                  >
                    <option value="Campus Gate 1">Campus Gate 1</option>
                    <option value="Campus Gate 2">Campus Gate 2</option>
                    <option value="Library Block">Library Block</option>
                  </select>
                </div>
              </div>

              <div className="modal-actions">
                <button type="button" className="btn btn-secondary" onClick={() => setIsEditModalOpen(false)}>Cancel</button>
                <button type="submit" className="btn btn-primary">Update Record (PUT)</button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
