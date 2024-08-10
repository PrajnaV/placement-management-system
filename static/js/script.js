document.addEventListener('DOMContentLoaded', function () {
    var studentModal = document.getElementById('studentModal');

    studentModal.addEventListener('show.bs.modal', function (event) {
      // Get the button that triggered the modal
      var button = event.relatedTarget;
      
      // Extract information from data attributes
      var studentName = button.getAttribute('data-student-name');
      var studentEmail = button.getAttribute('data-student-email');
      var studentImage = button.getAttribute('data-student-image');
      var studentPhone = button.getAttribute('data-student-phone');
      var studentBio = button.getAttribute('data-student-bio');
      var studentBranch = button.getAttribute('data-student-branch');
      var studentGender = button.getAttribute('data-student-gender');
      var studentSkills = button.getAttribute('data-student-skills');
      var studentCgpa = button.getAttribute('data-student-cgpa');
      var studentDegree = button.getAttribute('data-student-degree');
      
      // Update the modal's content
      var modalTitle = studentModal.querySelector('.modal-title');
      var studentNameField = studentModal.querySelector('#studentName');
      var studentEmailField = studentModal.querySelector('#studentEmail');
      var studentImageField = studentModal.querySelector('#studentImage');
      var studentPhoneField = studentModal.querySelector('#studentPhone');
      var studentBioField = studentModal.querySelector('#studentBio');
      var studentBranchField = studentModal.querySelector('#studentBranch');
      var studentGenderField = studentModal.querySelector('#studentGender');
      var studentSkillsField = studentModal.querySelector('#studentSkills');
      var studentCgpaField = studentModal.querySelector('#studentCgpa');
      var studentDegreeField = studentModal.querySelector('#studentDegree');
      
      studentNameField.textContent = studentName;
      studentEmailField.textContent = studentEmail;
      studentImageField.src = studentImage;
      studentPhoneField.textContent = studentPhone;
      studentBioField.textContent = studentBio;
      studentBranchField.textContent = studentBranch;
      studentGenderField.textContent = studentGender;
      studentSkillsField.textContent = studentSkills;
      studentCgpaField.textContent = studentCgpa;
      studentDegreeField.textContent = studentDegree;

    });
  });