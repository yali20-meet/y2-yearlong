document.addEventListener('musickitloaded', function() {
  // MusicKit global is now defined
  MusicKit.configure({
    developerToken: 'DEVELOPER-TOKEN',
    app: {
      name: 'My Cool Web App',
      build: '1978.4.1'
    }
  });
});